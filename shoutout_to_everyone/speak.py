import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

people = ["gautam", "james", "jessica", "jess"]
for person in people:
    print(person)
    speaker.Speak(f'Shoutout to {person}!')