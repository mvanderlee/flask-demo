from dataclasses import MISSING, field
from typing import Any, Callable, Dict


def required_field(
    default: Any = None,
    default_factory: Callable = MISSING,
    dump_only: bool = False,
    load_only: bool = False,
    help: str = None,
    filterable: bool = True,
    # Marshmallow Schema metadata
    metadata: Dict[str, Any] = None,
    # Marshmallow Schema kwargs
    **schema_kwargs,
):
    if default_factory != MISSING and default is None:
        default = MISSING

    return field(
        default=default,
        default_factory=default_factory,
        metadata=dict(
            **{} if schema_kwargs is None else schema_kwargs,
            required=True,
            dump_only=dump_only,
            load_only=load_only,
            metadata=dict(
                **{} if metadata is None else metadata,
                help=help,
                filterable=filterable,
            ),
        ),
    )
