from owlready2 import *
from graphviz import Digraph
from contextlib import contextmanager

@contextmanager
def editing(onto):
    with onto:
        yield
    onto.save(file="build/latest.ttl", format="turtle")

def classify():
    from owlready2 import sync_reasoner
    sync_reasoner()

def show_subclasses(cls):
    return [c for c in cls.subclasses()]

def add_disjoint(*classes):
    AllDisjoint([*classes])


def get_tree(ontos):
    g = Digraph("classes", graph_attr={"rankdir":"TB"})
    
    all_classes = []
    all_names = {}
    for onto in ontos if isinstance(ontos, list) else [ontos]:
        classes = list(onto.classes())
        names = {c: c.name for c in classes}
        all_classes.extend(classes)
        all_names.update(names)
    classes = set(all_classes)
    names = all_names
    
    for c in classes:
        if not names[c]:
            names[c] = f"{c.iri.split('#')[-1]}"
        g.node(names[c])
    
    for c in classes:
        for parent in c.is_a:
            if isinstance(parent, ThingClass) and parent in classes:
                g.edge(names[parent], names[c])

    return g

def onto_class_tree(onto):
    g = Digraph("sulo_classes", graph_attr={"rankdir":"TB"})
    classes = list(onto.classes())
    names = {c: c.name for c in classes}
    for c in classes: g.node(names[c])
    for c in classes:
        for parent in c.is_a:
            if isinstance(parent, ThingClass) and parent in classes:
                g.edge(names[parent], names[c])
    return g

# ---- helper: property map (domain -> property -> range) ----
def onto_property_map(onto):
    g = Digraph("sulo_props", graph_attr={"rankdir":"LR"})
    for p in onto.object_properties():
        domains = p.domain or [Thing]
        ranges  = p.range  or [Thing]
        
        for d in domains:
            for r in ranges:
                # check if d has an Or class
                if isinstance(d, Or):
                    for dd in d.Classes:
                        g.edge(dd.name, r.name, label=p.name)
                elif isinstance(r, Or):
                    for rr in r.Classes:
                        g.edge(d.name, rr.name, label=p.name)
                else:
                    g.edge(d.name, r.name, label=p.name)
    return g

from contextlib import redirect_stdout, redirect_stderr
def callReasoner(onto=None):
    with open('/dev/null', 'w') as f, redirect_stdout(f), redirect_stderr(f):
        with onto:
            sync_reasoner(ignore_unsupported_datatypes=True)
            return list(onto.inconsistent_classes())

def in_ancestors(onto, cls, ancestor):
    callReasoner(onto)
    if ancestor in cls.ancestors():
        print(f"{cls.name} is a subclass of {ancestor.name}")
    else:
        print(f"{cls.name} is NOT a subclass of {ancestor.name}")
