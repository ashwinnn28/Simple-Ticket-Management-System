import csv
import random
import pandas as pd

class Theater:
    def __init__(self, name, capacity, shows):
        self.name = name
        self.capacity = capacity
        self.shows = shows
        self.movies = []

class Ticket:
    def __init__(self, ticket_number, seat_number, theater_name, movie_name, show_time, ticket_type, price):
        self.ticket_number = ticket_number
        self.seat_number = seat_number
        self.theater_name = theater_name
        self.movie_name = movie_name
        self.show_time = show_time
        self.ticket_type = ticket_type
        self.price = price

class TicketingSystem:
    def __init__(self):
        self.theaters = []
        self.issued_tickets = []
        self.revenue = 0 

    def issue_ticket(self, theater_name, seat_number, movie_name, show_time, ticket_type):
        # Validate movie name
        allowed_movies = ["leo", "Batman", "Interstellar", "Avengers", "Inception","KGF", "Oppenheimer", "Titanic", "Spiderman", "Joker"]
        if movie_name not in allowed_movies:
            print("Enter a valid movie name.")
            return None

        # Validate show time
        allowed_show_times = ["9:30 AM", "1:30 PM", "6:00 PM"]
        if show_time not in allowed_show_times:
            print("Enter a valid show time (9:30 AM, 1:30 PM, 6:00 PM).")
            return None

        # Simulating ticket issuance with a random ticket number and price
        ticket_number = random.randint(1000, 9999)
        price = self.calculate_ticket_price(ticket_type)
        self.revenue += price
        ticket = Ticket(ticket_number, seat_number, theater_name, movie_name, show_time, ticket_type, price)

        # Update theater information
        theater = next((t for t in self.theaters if t.name == theater_name), None)
        if theater:
            theater.movies.append(movie_name)
        
        # Record the issued ticket for later revenue calculation
        self.issued_tickets.append(ticket)
        return ticket

    def calculate_ticket_price(self, ticket_type):
        # Simulating different ticket prices based on type
        if ticket_type == "I":
            return 100
        elif ticket_type == "II":
            return 150
        elif ticket_type == "III":
            return 200
        else:
            return 0

    def list_movies_in_theater(self, theater_name):
        theater = next((t for t in self.theaters if t.name == theater_name), None)
        if theater:
            return theater.movies[:5]  # Return the first 5 movies in the theater
        else:
            return []

    def list_all_movies(self):
        all_movies = set()
        for theater in self.theaters:
            all_movies.update(theater.movies)
        return list(all_movies)[:10]  # Return the first 10 movies

    def list_all_theaters_with_shows(self, movie_name):
        theaters_with_shows = []
        for theater in self.theaters:
            if movie_name in theater.movies:
                theaters_with_shows.append((theater.name, theater.shows))
        return theaters_with_shows

    def generate_revenue_report(self):
        report = []

    for theater in self.theaters:
        for show_time in theater.shows:
            # Calculate revenue for each show in each theater
            total_amount_sold = 0

            for ticket in self.issued_tickets:
                if ticket.theater_name == theater.name and ticket.show_time == show_time:
                    total_amount_sold += ticket.price

            report.append((theater.name, show_time, total_amount_sold))

    # Export to CSV
    with open('revenue_report.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Theater', 'Show Time', 'Total Amount Sold'])
        csv_writer.writerows(report)

    # Export to Excel
    df = pd.DataFrame(report, columns=['Theater', 'Show Time', 'Total Amount Sold'])
    df.to_excel('revenue_report.xlsx', index=False)

    return report


def main():
    # Initialize the ticketing system with two theaters
    # Update the initialization of theaters and shows
    theater_a = Theater("A", 50, ["9:30 AM", "1:30 PM", "6:00 PM"])
    theater_b = Theater("B", 25, ["9:30 AM", "1:30 PM", "6:00 PM"])

# Adding more movies to theaters
    theater_a.movies.extend(["leo", "Batman", "Interstellar", "Avengers", "Inception"])
    theater_b.movies.extend(["KGF", "Oppenheimer", "Titanic", "Spiderman", "Joker"])


    ticketing_system = TicketingSystem()
    ticketing_system.theaters.extend([theater_a, theater_b])

    while True:
        print("\n======== Ticket Management System =======")
        print("1. Issue Ticket")
        print("2. List Movies in a Theater")
        print("3. List All Movies")
        print("4. List Theaters with Shows for a Movie")
        print("5. Generate Revenue Report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            theater_name = input("Enter theater name (A/B): ")
            seat_number = input("Enter seat number (optional): ")
            movie_name = input("Enter movie name : ")

            # Validate movie name
            allowed_movies = ["leo", "Batman", "Interstellar", "Avengers", "Inception","KGF", "Oppenheimer", "Titanic", "Spiderman", "Joker"]
            if movie_name not in allowed_movies:
                print("Enter a valid movie name.")
                continue  # Move back to the main menu

            show_time = input("Enter show time (9:30 AM, 1:30 PM, 6:00 PM): ")
            
            # Validate show time only if the movie name is valid
            allowed_show_times = ["9:30 AM", "1:30 PM", "6:00 PM"]
            if show_time not in allowed_show_times:
                print("Enter a valid show time (9:30 AM, 1:30 PM, 6:00 PM).")
                continue  # Move back to the main menu

            ticket_type = input("Enter ticket type (I/II/III): ")

            ticket = ticketing_system.issue_ticket(theater_name, seat_number, movie_name, show_time, ticket_type)

            if ticket:
                print("\nTicket Issued Successfully:")
                print("Ticket Number:", ticket.ticket_number)
                print("Seat Number:", ticket.seat_number)
                print("Theater Name:", ticket.theater_name)
                print("Movie Name:", ticket.movie_name)
                print("Show Time:", ticket.show_time)
                print("Ticket Type:", ticket.ticket_type)
                print("Price:", ticket.price)

        # ... (rest of the menu options)

        elif choice == "2":
            theater_name = input("Enter theater name (A/B): ")
            movies = ticketing_system.list_movies_in_theater(theater_name)
            if movies:
                print(f"Movies in {theater_name} Theater: {', '.join(movies)}")
            else:
                print(f"No movies found in {theater_name} Theater.")

        elif choice == "3":
            all_movies = ticketing_system.list_all_movies()
            print("All Movies: ", ', '.join(all_movies))

        elif choice == "4":
            movie_name = input("Enter movie name: ")
            theaters_with_shows = ticketing_system.list_all_theaters_with_shows(movie_name)
            if theaters_with_shows:
                print(f"Theaters with Shows for {movie_name}:")
                for theater, shows in theaters_with_shows:
                    print(f"{theater}: {', '.join(shows)}")
            else:
                print(f"No theaters found with shows for {movie_name}.")

        elif choice == "5":
            revenue_report = ticketing_system.generate_revenue_report()
            print("\n Revenue Report:")
            for theater, show_time, total_amount_sold in revenue_report:
                print(f"{theater}, {show_time} show, {total_amount_sold} Rs")

        elif choice == "0":
            print("Exiting the Ticket Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
