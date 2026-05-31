from database.db_manager import (
    clear_prediction_history,
    get_prediction_history
)

clear_prediction_history()

history = get_prediction_history()

print("Rows After Clear:")
print(history)
print("Total Rows:", len(history))