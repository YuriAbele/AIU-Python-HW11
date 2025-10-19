from datetime import datetime
from tests import test_nested_imports

SPLIT_LINE = "\n" + "#" * 100 + "\n"

print("")

print(SPLIT_LINE)

# полная проверка
test_nested_imports()

print(SPLIT_LINE)
print(f"\n{"="*50}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
