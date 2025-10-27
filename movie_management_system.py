def calculate_ticket_revenue(show_type, tickets_sold, time_slot):
    
    tickets_sold = int(tickets_sold)
    if show_type == 'blockbuster' or show_type == 'BLOCKBUSTER':
        if time_slot == 'morning' or time_slot == 'MORNING':
           
            return 12 * tickets_sold
        
        if time_slot == 'afternoon' or time_slot == 'AFTERNOON':
            
            return 18 * tickets_sold
        
        if time_slot == 'evening' or time_slot == 'EVENING':
            
            return 25 * tickets_sold
        
    elif show_type == 'standard' or show_type == 'STANDARD':
        if time_slot == 'morning' or time_slot == 'MORNING':
            
            return 8 * tickets_sold
        
        if time_slot == 'afternoon' or time_slot == 'AFTERNOON':
            
            return 12 * tickets_sold
        
        if time_slot == 'evening' or time_slot == 'EVENING':
            
            return 16 * tickets_sold
        
    elif show_type == 'classic' or show_type == 'CLASSIC':
        if time_slot == 'morning' or time_slot == 'MORNING':
            
            return 5 * tickets_sold
        
        if time_slot == 'afternoon' or time_slot == 'AFTERNOON':
            
            return 8 * tickets_sold
        
        if time_slot == 'evening' or time_slot == 'EVENING':
            
            return 10 * tickets_sold
        else:
            print('Please check your input(morning, afternoon, evening) ')
    else:
        print('Please check your input(Try one of these; blockbuster, standard, classic)')
        
    

def calculate_occupancy_rate(theater_years, baseline_seats, filled_seats):
    capacity = 1000 + (theater_years * 100)
    seat_availability = capacity - baseline_seats
    occupancy_percentage = (filled_seats - baseline_seats) / seat_availability * 100

    return occupancy_percentage

def determine_popularity_status(occupancy_percent):
    if occupancy_percent < 50:
        return 'Low Demand'
    elif occupancy_percent <= 60:
        return 'Moderate Demand'
    elif occupancy_percent < 70:
        return 'Good Demand'
    elif occupancy_percent <= 85:
        return 'High Demand'
    elif occupancy_percent <= 100:
        return 'Sold Out Status'
    
def calculate_total_profit(revenue, tickets, status_multiplier):
    profit = revenue * 0.05 + tickets * 2

    if status_multiplier == 'Low Demand':
        status_multi = 0.5
    elif status_multiplier == 'Moderate Demand':
        status_multi = 1.0
    elif status_multiplier == 'Good Demand':
        status_multi = 1.2
    elif status_multiplier == 'High Demand':
        status_multi = 1.5
    elif status_multiplier == 'Sold Out Status':
        status_multi = 1.8
    else:
        status_multi = 1.0
        

        
    return round(profit * status_multi, 1)

def needs_promotion(screening_days, total_tickets, avg_occupancy):
    if screening_days >= 6 and avg_occupancy < 50:
        return 'Yes'
    elif total_tickets < 100 and avg_occupancy < 60:
        return 'Yes'
    elif screening_days >= 4 and avg_occupancy < 40:
        return 'Yes'
    else:
        return 'No'
    
def generate_theater_report(movie_title, show_type, tickets, time_slot, theater_years, baseline_seats, filled_seats, screening_days):
    print('MOVIE THEATER MANAGEMENT SYSTEM')
    print('=' * 40)
    print(f"Theater Report for: {movie_title}")
    print('-' * 40)
    print(f'Show Type: {show_type}')
    print(f"Tickets Sold: {tickets}")
    print(f"Time Slot: {time_slot}")
    
    revenue = calculate_ticket_revenue(show_type, tickets, time_slot)
    occupancy_analys = calculate_occupancy_rate(theater_years, baseline_seats, filled_seats)
    rate = determine_popularity_status(occupancy_analys)
    total_profit = calculate_total_profit(revenue, tickets, rate )
    is_need_promotion = needs_promotion(screening_days, tickets, occupancy_analys)
    print(f"Ticket Revenue: ${revenue}")
    print('Occupancy Analysis')
    
    print(f"  Experience: {theater_years} years, Baseline: {baseline_seats}, Filled Seats: {filled_seats}")
    print(f"  Occupancy: {occupancy_analys:.1f}%")
    print(f"  Popularity Status: {rate}")
    print(f"Total profit: ${total_profit:.1f}")
    print(f"Screening days: {screening_days}")
    print(f"Promotion needed: {is_need_promotion}")

generate_theater_report('Space', 'blockbuster', 45, 'evening', 3, 800, 1150, 3)
generate_theater_report('Comedy Night', 'standard', 60,'afternoon', 5, 900, 1300, 5)
generate_theater_report('Old Classic', 'classic', 30, 'morning', 8, 850, 950, 7)



