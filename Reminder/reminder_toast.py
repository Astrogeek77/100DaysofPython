try:
    from win10toast import ToastNotifier
    import time
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    curr_path = "C:\\Coding\\Python\\100DaysofCode\\Reminder"

    def countdown(t):
        while t >= 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def speak_message(reminder_title, reminder_desc):
        speaker.speak(f"Reminder {reminder_title}, {reminder_desc}")

    def show_notification(reminder_title, reminder_desc, mins):
        mins = mins * 10

        countdown(mins)
        # time.sleep(mins)

        toast = ToastNotifier()

        toast.show_toast(
            reminder_title,
            reminder_desc,
            duration=5,
            icon_path=f"{curr_path}\\icons\\custom-icon.ico"
        )

        speak_message(reminder_title, reminder_desc)

    reminder_title = input("Title of the Reminder: ")
    reminder_desc = input("Description of the Reminder: ")
    user_input = int(input("Set Timer (in minutes) for reminder: "))

    # reminder_title = "Stay hydrated and healthy"
    # reminder_desc = "Drink a glass of water now"
    # user_input = 1

    # speak_message(reminder_title, reminder_desc)
    show_notification(reminder_title, reminder_desc, user_input)

except Exception as e:
    print(e)
