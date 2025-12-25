from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass(frozen=True)
class Document:
    # Mengelompokkan data terkait dalam satu objek
    text: str
    vector: List[float]
    id: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        # Validasi sederhana saat objek dibuat
        if not self.text.strip():
            raise ValueError('Text must not be empty')
        
        if len(self.vector) != 128:
            raise ValueError(f'Vector dimension must be 128, current value: {len(self.vector)}')