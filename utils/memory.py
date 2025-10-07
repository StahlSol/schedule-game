# utils/memory.py

def decay_memory(cheff, decay_per_hour: int = 5):
    """
    Reduce Cheff's memory/freshness over time.
    """
    cheff.memory -= decay_per_hour
    if cheff.memory < 0:
        cheff.memory = 0
    elif cheff.memory > 100:
        cheff.memory = 100
