from cvs_handler import CVS
from generare_buget import EventBudget

CVS.initialize_csv()
event_budget = EventBudget(CVS.read_entries())
# event_budget.print_variables()
event_budget.calculeaza_buget()

