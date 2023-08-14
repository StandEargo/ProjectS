from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from datetime import datetime, timedelta
import calendar

class CalendarApp(App):
    def build(self):
        layout = GridLayout(cols=7)
        
        days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for day in days:
            label = Label(text=day)
            layout.add_widget(label)
        
        today = datetime.today()
        year = today.year
        month = today.month
        num_days = calendar.monthrange(year, month)[1]
        
        first_day_of_month = today.replace(day=1)
        day_offset = first_day_of_month.weekday()
        
        for _ in range(day_offset):
            layout.add_widget(Label(text=''))
        
        for day_num in range(1, num_days + 1):
            day_label = Label(text=str(day_num))
            layout.add_widget(day_label)
        
        for _ in range(6 - (day_offset + num_days) % 7):
            layout.add_widget(Label(text=''))
        
        holidays = [10, 15]  # Example holidays on the 10th and 15th of the month
        
        for holiday in holidays:
            layout.children[(day_offset + holiday) + 7].color = (1, 0, 0, 1)
        
        return layout

if __name__ == '__main__':
    CalendarApp().run()