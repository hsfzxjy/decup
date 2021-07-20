from typing import TypeVar, Any, Callable, ContextManager, Dict, Tuple, overload

_T = TypeVar("_T")
_U = TypeVar("_U")
_F = TypeVar("_F")

class Var:
    def __getattr__(self, name: str) -> "Var": ...
    def __getitem__(self, attr: str) -> "Var": ...

class _V:
    def __getattr__(self, name: str) -> Var: ...

class _S:
    def assign(self, var: _T, value: _U) -> _U: ...
    def isvar(self, var: Var) -> bool: ...
    def isempty(self, var: Var) -> bool: ...
    def inject(self, func: _F) -> _F: ...
    @overload
    def patch(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def patch(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...
    @overload
    def patch_local(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def patch_local(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...
    @overload
    def isolate(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def isolate(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...
    @overload
    def isolate_local(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def isolate_local(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...
    @overload
    def shield(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def shield(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...
    @overload
    def shield_local(self, *vars: Tuple[Var]) -> ContextManager: ...
    @overload
    def shield_local(self, var_mapping: Dict[Var, Any]) -> ContextManager: ...

S: _S
V: _V