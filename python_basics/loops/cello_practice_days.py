# cello_practice_days.py
# 🎻 Count how many days I practiced cello this week — real life edition 💪

print("🎻 Cello Practice Tracker — Reality Check Edition")

print("""
This program helps track how many days I managed to practice cello this week,
while also...
🧑‍🏫 Working full-time at Latin School of Chicago
🎼 Teaching at CML
🎻 Playing in Lakeshore Symphony Orchestra
🎻 Playing in Chicago Metropolitan Symphony Orchestra
🎻 Rehearsing with Four Seasons Chamber Music Society
🧠 Studying IT
💼 Applying for entry-level IT jobs
🧗‍♀️ Indoor rock climbing and working out
😅 Somehow surviving...
""")

day = 1
practice_days = 0

while day <= 7:
    practiced = input(f"Day {day}: Did you practice cello? (y/n): ").lower()
    if practiced == "y":
        practice_days += 1
    day += 1

print(f"\n🎉 You practiced cello on {practice_days} day(s) this week!")
print("Yay, go me! 🎈🎻")
