def accomodation():
    total_rooms = int(input())

    count = 0
    while total_rooms > 0:
        people_in_room, room_capacity = map(int, input().split())
        if room_capacity - people_in_room >= 2:
            count += 1
        total_rooms -= 1
    return count

print(accomodation())
