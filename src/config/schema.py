from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LevelConfig:
    """Per-level parameters (Parser guarantees these are valid)."""

    name: str
    width: int
    height: int
    pacgum: int
    seed: int | float | str | bytes | bytearray | None
    level_max_time: int


@dataclass(frozen=True)
class Config:
    """Validated, ready-to-use game configuration."""

    highscore_filename: str
    levels: list[LevelConfig]
    lives: int
    points_per_pacgum: int
    points_per_superpacgum: int
    points_per_ghost: int

    @staticmethod
    def from_dict(raw: dict[str, Any]) -> Config:
        """Wrap Parser's dict into typed dataclasses."""
        levels = [
            LevelConfig(
                name=lvl.get("name", f"level{i + 1}"),
                width=lvl["width"],
                height=lvl["height"],
                pacgum=lvl["pacgum"],
                seed=lvl.get("seed"),
                level_max_time=lvl["level_max_time"],
            )
            for i, lvl in enumerate(raw["levels"])
        ]
        return Config(
            highscore_filename=raw["highscore_filename"],
            levels=levels,
            lives=raw["lives"],
            points_per_pacgum=raw["points_per_pacgum"],
            points_per_superpacgum=raw["points_per_superpacgum"],
            points_per_ghost=raw["points_per_ghost"],
        )
