# Train Reservation System in Python

class Train:
    def __init__(self, train_number, train_name, source, destination, total_seats):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
    
    def book_ticket(self, num_seats):
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            print(f"\n{num_seats} ticket(s) booked successfully!")
            print(f"Available seats: {self.available_seats}")
            return True
        else:
            print(f"\nSorry! Only {self.available_seats} seats available")
            return False
    
    def cancel_ticket(self, num_seats):
        if self.available_seats + num_seats <= self.total_seats:
            self.available_seats += num_seats
            print(f"\n{num_seats} ticket(s) cancelled successfully!")
            print(f"Available seats: {self.available_seats}")
        else:
            print("\nInvalid cancellation")
    
    def display_info(self):
        print(f"\nTrain Number: {self.train_number}")
        print(f"Train Name: {self.train_name}")
        print(f"Route: {self.source} to {self.destination}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

# Main
if __name__ == "__main__":
    train = Train("12345", "Express", "Mumbai", "Delhi", 100)
    train.display_info()
    train.book_ticket(5)
    train.book_ticket(3)
    train.cancel_ticket(2)
    train.display_info()
