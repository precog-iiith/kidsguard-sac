class Constants:

	class DataType:
		class Balanced:
			TYPE = 'balanced_data'
			NUM_CLASSES = 4
		class Unbalanced:
			TYPE = 'unbalanced_data'
			NUM_CLASSES = 4
		class Safe:
			TYPE = 'safe_data'
			NUM_CLASSES = 2
		class Explicit:
			TYPE = 'explicit_data'
			NUM_CLASSES = 3

	class SecondsPerClip:
		ONE_SEC = 1
		THREE_SEC = 3
		FIVE_SEC = 5
		TEN_SEC = 10