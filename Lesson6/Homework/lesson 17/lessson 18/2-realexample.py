aliens = []

for alien in range(30):
    new_alien = {
        "color": "green",
        "point": 5,
        "speed": "slow"
    }
    aliens.append(new_alien)
    
    for alien in aliens[:5]:
        print(alien)
    print("...")
    print(f"totla number of alien's is {len(aliens)}")