bird(canary).
bird(sparrow).
bird(ostrich).
bird(penguin).

can_fly(canary).
can_fly(sparrow).
flies(X) :- bird(X), can_fly(X).
