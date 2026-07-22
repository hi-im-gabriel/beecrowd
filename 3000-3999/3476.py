def calculate_completion_time(samaro_days, bomdebrecha_days, corria_days):
  inverse_rate = 1 / samaro_days + 1 / bomdebrecha_days + 1 / corria_days
  completion_time = 1 / inverse_rate
  return completion_time

samaro_days, bomdebrecha_days, corria_days = map(int, input().split())

result = calculate_completion_time(samaro_days, bomdebrecha_days, corria_days)
print(f"{result:.3f}")
