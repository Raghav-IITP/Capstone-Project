import mysql.connector
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1319x600+200+230")
        self.root.configure(bg="white")

        self.label_font = ("Helvetica", 14, "bold")
        self.card_font = ("Helvetica", 16, "bold")
        self.card_colors = {
            "bookings": "#ff7f7f",
            "available": "#ffa07a",
            "booked": "#ff1493",
            "visitors": "#00ced1"
        }

        self.room_types = ["Single", "Double", "Triple", "Deluxe", "Suite", "Studio"]
        self.occupancy_percentages = [33, 67, 30, 40, 10, 15]
        self.colors = ["#800080", "#00ced1", "#3eb489", "#ff6f61", "#ff1493", "#e34234"]

        self.setup_ui()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@3115", database="sys")
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM bookings")
        total_bookings = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM rooms WHERE status='Available'")
        available_rooms = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM rooms WHERE status='Booked'")
        booked_rooms = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM visitors")
        total_visitors = cursor.fetchone()[0]

        room_counts = []
        for room in self.room_types:
            cursor.execute(f"SELECT COUNT(*) FROM rooms WHERE room_type='{room}'")
            room_counts.append(cursor.fetchone()[0])

        conn.close()
        return total_bookings, available_rooms, booked_rooms, total_visitors, room_counts

    def fetch_visitors_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mysql@3115", database="sys")
        cursor = conn.cursor()

        cursor.execute("SELECT visit_date, COUNT(*) FROM visitors GROUP BY visit_date")
        visitors_data = cursor.fetchall()

        conn.close()

        dates = [row[0] for row in visitors_data]
        counts = [row[1] for row in visitors_data]

        return dates, counts

    def create_card(self, parent, title, value, color, row, column):
        card = tk.Frame(parent, bg=color, bd=5, relief="ridge", width=200, height=100)
        card.grid(row=row, column=column, padx=15, pady=10)

        label_title = tk.Label(card, text=title, font=self.label_font, bg=color, fg="#ffffff")
        label_title.pack(pady=(10, 5))

        label_value = tk.Label(card, text=value, font=self.card_font, bg=color, fg="#ffffff")
        label_value.pack()

        return card

    def create_donut_chart(self, room_type, count, color, row, col):
        fig, ax = plt.subplots(figsize=(2.5, 2.5))
        values = [count, 100 - count]
        wedges, texts = ax.pie(values, wedgeprops=dict(width=0.3), startangle=90, colors=[color, "#dfe6e9"])
        ax.text(0, 0.1, room_type, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(0, -0.2, f"{count}%", ha='center', va='center', fontsize=12, fontweight='bold')
        ax.set_aspect("equal")

        canvas = FigureCanvasTkAgg(fig, master=self.progress_frame)
        canvas.get_tk_widget().grid(row=row, column=col, padx=15, pady=10)

    def setup_ui(self):
        tk.Label(self.root, text="Dashboard", font=("Segoe UI", 24, "bold"), bg="white", fg="#2c3e50").pack(anchor="nw", padx=20, pady=(10, 0))

        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(pady=20)

        self.graph_card = tk.Frame(self.main_frame, bg="#ffdde4", bd=5, relief="ridge", width=800, height=300)
        self.graph_card.grid(row=1, column=0, columnspan=4, pady=20)

        total_bookings, available_rooms, booked_rooms, total_visitors, _ = self.fetch_data()
        self.create_card(self.main_frame, "New Bookings", total_bookings, self.card_colors["bookings"], 0, 0)
        self.create_card(self.main_frame, "Available Rooms", available_rooms, self.card_colors["available"], 0, 1)
        self.create_card(self.main_frame, "Booked Rooms", booked_rooms, self.card_colors["booked"], 0, 2)
        self.create_card(self.main_frame, "Total Visitors", total_visitors, self.card_colors["visitors"], 0, 3)

        self.progress_frame = tk.Frame(self.root, bg="white")
        self.progress_frame.pack(pady=20)

        for i, (rtype, percent) in enumerate(zip(self.room_types, self.occupancy_percentages)):
            self.create_donut_chart(rtype, percent, self.colors[i % len(self.colors)], 0, i)

        self.plot_visitor_graph()

    def plot_visitor_graph(self):
        visitor_dates, visitor_counts = self.fetch_visitors_data()
        fig_line, ax_line = plt.subplots(figsize=(8, 3))
        ax_line.plot(visitor_dates, visitor_counts, marker="o", linestyle="-", color="deeppink", linewidth=2, markersize=6)
        ax_line.set_title("Visitors Per Day")
        ax_line.set_xlabel("Date")
        ax_line.set_ylabel("Number of Visitors")
        ax_line.grid(True, linestyle="--", alpha=0.7)
        ax_line.tick_params(axis='x', rotation=45)

        fig_line.tight_layout()
        canvas_line = FigureCanvasTkAgg(fig_line, master=self.graph_card)
        canvas_line.draw()
        canvas_line.get_tk_widget().pack(pady=10, padx=10, anchor="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()