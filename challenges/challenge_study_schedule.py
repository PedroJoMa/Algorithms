def study_schedule(permanence_period, target_time):
    # permanence period [(entrada, saída)] target_time(tempo_alvo)
    try:
        counter = 0
        for period in permanence_period:
            start_time, end_time = period
            if start_time <= target_time <= end_time:
                counter += 1
        return counter
    except TypeError:
        return None
