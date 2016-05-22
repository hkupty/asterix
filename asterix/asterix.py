# encoding: utf-8
from collections import defaultdict, namedtuple

component = namedtuple("Component", ("dependency_set", "start_command"))

def all_deps_started(c, t): return (c & t) == c

def run_hooks(hooks):
    for hook in hooks.get(k, []):
        code = hook.__code__
        argc, argn = code.co_argcount, code.co_varnames

        args = {
            m: started_components[m]
            for m
            in argn[:argc]
        }

        hook(**args)


def start_components(components, deps_graph, k, started_components={}):
    dependencies, command = components.get(k, (set(), None))
    if all_deps_started(dependencies, started_components.keys()):
        if k:
            component = command(
                **{i: started_components[i] for i in dependencies}
            )

            started_components[k] = component

        for j in deps_graph[k]:
            started_components = start_components(
                components, deps_graph, j, started_components
            )
    return started_components

def build_deps_graph(components):
    deps = defaultdict(set)

    for k, v in components.items():
        if len(v[0]) == 0:
            deps[None].add(k)
        else:
            [deps[i].add(k) for i in v[0]]

    return deps


def start_system(components, bind_to, hooks={}):
    """Start all components on component map."""
    deps = build_deps_graph(components)
    started_components = start_components(components, deps, None)

    run_hooks(hooks)

    if type(bind_to) is str:
        master = started_components[bind_to]
    else:
        master = bind_to

    setattr(master, '__components', started_components)
    return master


def get_component(name, master):
    return master.__components.get(name, None)
