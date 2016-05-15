# encoding: utf-8
from collections import defaultdict

def all_deps_started(c, t): return (c & t) == c


def start_system(components, bind_to, hooks={}):
    """Start all components on component map."""
    deps = defaultdict(set)
    started_components = {}

    def start(k):
        dependencies, command = components[k]
        if all_deps_started(dependencies, started_components.keys()):
            component = command(
                **{i: started_components[i] for i in dependencies}
            )

            started_components[k] = component

            for hook in hooks:
                code = hook.__code__
                argc, argn = code.co_argcount, code.co_varnames

                print(started_components, argc, argn, sep=", ")

                args = {
                    m: started_components[m]
                    for m
                    in argn[:argc]
                }

                hook(**args)

            for j in deps[k]:
                start(j)

    for k, v in components.items():
        if len(v[0]) == 0:
            deps[None].add(k)
        else:
            [deps[i].add(k) for i in v[0]]

    [start(i) for i in deps[None]]

    if type(bind_to) is str:
        master = started_components[bind_to]
    else:
        master = bind_to

    setattr(master, '__components', started_components)
    return master


def get_component(name, master):
    return master.__components.get(name, None)
