import threading

def handle_request(request):
    # ประมวลผลคำขอ
    print(f"Handling request: {request}")
    # สมมติว่าต้องใช้เวลาสักครู่ในการประมวลผล
    import time
    time.sleep(1)
    print(f"Finished request: {request}")

# จำลองคำขอจากผู้ใช้หลายๆ คำขอ
requests = ["Request 1", "Request 2", "Request 3", "Request 4"]

# สร้างเธรดสำหรับแต่ละคำขอ
threads = []
for request in requests:
    thread = threading.Thread(target=handle_request, args=(request,))
    threads.append(thread)

# รันเธรดทั้งหมด
for thread in threads:
    thread.start()

# รอให้เธรดทั้งหมดทำงานเสร็จสิ้น
for thread in threads:
    thread.join()

print("All requests handled.")
