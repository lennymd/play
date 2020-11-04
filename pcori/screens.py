# This is an attempt at trying to figure out all the screens I need to make

intervention = ["T", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]
need = ["N","N1","N2","N3","N4","N5","N6","N7","N8","N9","N10","N11","N12","N13","N14","N15","N16","N17","N18",
]
characteristics = ["C", "C1", "C2", "C3"]
outcomes = ["U","O1","O2","O3","O4","O5","O6","O7","O8","O9","O10","O11","O12","O13","O14","O15","O16","O17","O18","O19","O20","O21","O22","O23","O24","O25","O26","O27","O28",
]
quality = ["Q1", "Q2"]

print(len(intervention) * len(need) * len(characteristics) * len(outcomes) * len(quality)
)

all_options = ["T0","T1","T2","T3","T4","T5","T6","T7","T8","T9","N0","N1","N2","N3","N4","N5","N6","N7","N8","N9","N10","N11","N12","N13","N14","N15","N16","N17","N18","C0","C1","C2","C3","U0","U1","U2","U3","U4","U5","U6","U7","U8","U9","O10","O11","O12","O13","O14","O15","O16","O17","O18","O19","O20","O21","O22","O23","O24","O25","O26","O27","O28","Q1","Q2"]
