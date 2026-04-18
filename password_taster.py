#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════╗
║                    PASSWORD TASTER v2.0                            ║
║                  Professional Password Tool                        ║
║                      Author: Abdullah                              ║
╚════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import getpass

# Professional color scheme with backgrounds
class Style:
    # Reset
    RESET = '\033[0m'
    
    # Regular Colors
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Bold Colors
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Background Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_animation(text, delay=0.03):
    """Type animation effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    # Top border with background
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}╔══════════════════════════════════════════════════════════════════════════════════╗{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                                                                                  ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                     🔐 PASSWORD TASTER PROFESSIONAL EDITION 🔐                    ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                                                                                  ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                           Author: Abdullah                                      ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                           Version: 2.0                                           ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}║                                                                                  ║{Style.RESET}")
    print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}╚══════════════════════════════════════════════════════════════════════════════════╝{Style.RESET}")
    print()

def password_visual(password):
    """Show password with visual representation"""
    print(f"{Style.CYAN}{Style.BOLD}╔════════════════════════════════════════════════════════════════════╗{Style.RESET}")
    print(f"{Style.CYAN}{Style.BOLD}║                    YOUR ENTERED PASSWORD                           ║{Style.RESET}")
    print(f"{Style.CYAN}{Style.BOLD}╚════════════════════════════════════════════════════════════════════╝{Style.RESET}")
    
    # Show masked password with background
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD}  PASSWORD: {Style.RESET}", end="")
    for i, char in enumerate(password):
        if i < 2 or i >= len(password)-2:
            print(f"{Style.BG_GREEN}{Style.BLACK}{char}{Style.RESET}", end="")
        else:
            print(f"{Style.BG_YELLOW}{Style.BLACK}*{Style.RESET}", end="")
    print()
    
    # Show actual length
    print(f"{Style.BG_PURPLE}{Style.WHITE}  LENGTH: {len(password)} characters{Style.RESET}\n")

def analyze_password(password):
    """Professional password analysis"""
    score = 0
    max_score = 100
    criteria = []
    
    print(f"{Style.BG_BLUE}{Style.WHITE}{Style.BOLD}╔════════════════════════════════════════════════════════════════════╗{Style.RESET}")
    print(f"{Style.BG_BLUE}{Style.WHITE}{Style.BOLD}║                    SECURITY ANALYSIS IN PROGRESS...                 ║{Style.RESET}")
    print(f"{Style.BG_BLUE}{Style.WHITE}{Style.BOLD}╚════════════════════════════════════════════════════════════════════╝{Style.RESET}\n")
    
    time.sleep(1)
    
    # 1. Length Analysis
    length = len(password)
    print(f"{Style.BOLD}📏 LENGTH CHECK:{Style.RESET}")
    if length >= 16:
        score += 25
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ EXCELLENT {Style.RESET} {Style.GREEN}{length} characters (16+ recommended){Style.RESET}")
        criteria.append("Length: Excellent")
    elif length >= 12:
        score += 20
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ GOOD       {Style.RESET} {Style.GREEN}{length} characters{Style.RESET}")
        criteria.append("Length: Good")
    elif length >= 8:
        score += 10
        print(f"   {Style.BG_YELLOW}{Style.BLACK}  ⚠ ACCEPTABLE {Style.RESET} {Style.YELLOW}{length} characters (minimum){Style.RESET}")
        criteria.append("Length: Acceptable")
    else:
        score -= 10
        print(f"   {Style.BG_RED}{Style.WHITE}  ✗ WEAK       {Style.RESET} {Style.RED}{length} characters (need 8+){Style.RESET}")
        criteria.append("Length: Too Short")
    time.sleep(0.5)
    
    # 2. Numbers Check
    has_number = any(c.isdigit() for c in password)
    print(f"\n{Style.BOLD}🔢 NUMBERS CHECK:{Style.RESET}")
    if has_number:
        score += 20
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ INCLUDED   {Style.RESET} {Style.GREEN}Contains numbers{Style.RESET}")
        criteria.append("Numbers: Yes")
    else:
        print(f"   {Style.BG_RED}{Style.WHITE}  ✗ MISSING    {Style.RESET} {Style.RED}No numbers found{Style.RESET}")
        criteria.append("Numbers: No")
    time.sleep(0.5)
    
    # 3. Uppercase Check
    has_upper = any(c.isupper() for c in password)
    print(f"\n{Style.BOLD}🔠 UPPERCASE CHECK:{Style.RESET}")
    if has_upper:
        score += 20
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ INCLUDED   {Style.RESET} {Style.GREEN}Contains uppercase letters{Style.RESET}")
        criteria.append("Uppercase: Yes")
    else:
        print(f"   {Style.BG_RED}{Style.WHITE}  ✗ MISSING    {Style.RESET} {Style.RED}No uppercase letters{Style.RESET}")
        criteria.append("Uppercase: No")
    time.sleep(0.5)
    
    # 4. Lowercase Check
    has_lower = any(c.islower() for c in password)
    print(f"\n{Style.BOLD}🔡 LOWERCASE CHECK:{Style.RESET}")
    if has_lower:
        score += 15
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ INCLUDED   {Style.RESET} {Style.GREEN}Contains lowercase letters{Style.RESET}")
        criteria.append("Lowercase: Yes")
    else:
        print(f"   {Style.BG_RED}{Style.WHITE}  ✗ MISSING    {Style.RESET} {Style.RED}No lowercase letters{Style.RESET}")
        criteria.append("Lowercase: No")
    time.sleep(0.5)
    
    # 5. Special Characters Check
    specials = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    has_special = any(c in specials for c in password)
    print(f"\n{Style.BOLD}✨ SPECIAL CHARACTERS CHECK:{Style.RESET}")
    if has_special:
        score += 20
        print(f"   {Style.BG_GREEN}{Style.BLACK}  ✓ INCLUDED   {Style.RESET} {Style.GREEN}Contains special characters{Style.RESET}")
        criteria.append("Special: Yes")
    else:
        print(f"   {Style.BG_RED}{Style.WHITE}  ✗ MISSING    {Style.RESET} {Style.RED}No special characters{Style.RESET}")
        criteria.append("Special: No")
    time.sleep(0.5)
    
    # Ensure score is within bounds
    score = max(0, min(100, score))
    
    return score, criteria

def show_results(password, score, criteria):
    """Display professional results with background colors"""
    
    # Determine strength level and color
    if score >= 80:
        strength = "STRONG"
        color = Style.BG_GREEN
        text_color = Style.BLACK
        icon = "🔒"
        emoji = "✅"
        message = "EXCELLENT! This password is highly secure"
    elif score >= 60:
        strength = "MODERATE"
        color = Style.BG_YELLOW
        text_color = Style.BLACK
        icon = "⚠️"
        emoji = "📊"
        message = "Good but can be improved"
    elif score >= 40:
        strength = "WEAK"
        color = Style.BG_BRIGHT_YELLOW
        text_color = Style.BLACK
        icon = "⚠️"
        emoji = "🔧"
        message = "This password needs improvement"
    else:
        strength = "VERY WEAK"
        color = Style.BG_RED
        text_color = Style.WHITE
        icon = "❌"
        emoji = "🚨"
        message = "DANGER! This password is easily hackable"
    
    # Main results box
    print(f"\n{Style.BOLD}{Style.CYAN}╔════════════════════════════════════════════════════════════════════╗{Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN}║                    🔍 FINAL ANALYSIS RESULTS 🔍                    ║{Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN}╚════════════════════════════════════════════════════════════════════╝{Style.RESET}")
    
    # Password info
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD} PASSWORD INFO {Style.RESET}")
    print(f"  {Style.BOLD}Original:{Style.RESET} {Style.DIM}{password}{Style.RESET}")
    print(f"  {Style.BOLD}Length:{Style.RESET} {len(password)} characters")
    
    # Score with progress bar
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD} SECURITY SCORE {Style.RESET}")
    print(f"  {Style.BOLD}Score:{Style.RESET} {score}/100")
    
    # Progress bar
    bar_length = 40
    filled = int(bar_length * score / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    if score >= 70:
        bar_color = Style.GREEN
    elif score >= 40:
        bar_color = Style.YELLOW
    else:
        bar_color = Style.RED
    
    print(f"  [{bar_color}{bar}{Style.RESET}] {score}%")
    
    # Strength level with background
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD} STRENGTH LEVEL {Style.RESET}")
    print(f"  {color}{text_color}{Style.BOLD} {icon} {strength} {icon} {Style.RESET}")
    
    # Detailed criteria
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD} DETAILED CHECKLIST {Style.RESET}")
    for item in criteria:
        if "Yes" in item or "Excellent" in item or "Good" in item:
            print(f"  {Style.GREEN}✓{Style.RESET} {item}")
        elif "No" in item or "Short" in item:
            print(f"  {Style.RED}✗{Style.RESET} {item}")
        else:
            print(f"  {Style.YELLOW}⚠{Style.RESET} {item}")
    
    # Recommendations box
    print(f"\n{Style.BG_BLUE}{Style.WHITE}{Style.BOLD} RECOMMENDATIONS {Style.RESET}")
    print(f"  {emoji} {message}")
    
    if score < 80:
        print(f"  {Style.YELLOW}💡 Tips to improve:{Style.RESET}")
        if len(password) < 12:
            print(f"     • Make password longer (12+ characters)")
        if not any(c.isdigit() for c in password):
            print(f"     • Add numbers (0-9)")
        if not any(c.isupper() for c in password):
            print(f"     • Add uppercase letters (A-Z)")
        if not any(c.islower() for c in password):
            print(f"     • Add lowercase letters (a-z)")
        if not any(c in "!@#$%^&*()" for c in password):
            print(f"     • Add special characters (!@#$%^&*)")
    
    # Footer
    print(f"\n{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}⚡ Generated by Password Taster - Abdullah ⚡{Style.RESET}")

def main():
    try:
        while True:
            banner()
            
            # Instructions box
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}╔════════════════════════════════════════════════════════════════════╗{Style.RESET}")
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}║  INSTRUCTIONS:                                                     ║{Style.RESET}")
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}║  • Enter any password to check its strength                        ║{Style.RESET}")
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}║  • Password will be hidden for security                            ║{Style.RESET}")
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}║  • Get detailed analysis with professional report                  ║{Style.RESET}")
            print(f"{Style.BG_YELLOW}{Style.BLACK}{Style.BOLD}╚════════════════════════════════════════════════════════════════════╝{Style.RESET}")
            
            print()
            
            # Get password
            password = getpass.getpass(f"{Style.BOLD}{Style.CYAN}🔑 ENTER PASSWORD TO ANALYZE: {Style.RESET}")
            
            if not password:
                print(f"\n{Style.BG_RED}{Style.WHITE} ERROR: Password cannot be empty! {Style.RESET}")
                input(f"\n{Style.YELLOW}Press Enter to continue...{Style.RESET}")
                continue
            
            # Show the entered password (visual)
            password_visual(password)
            
            # Analyze
            score, criteria = analyze_password(password)
            
            # Show results
            show_results(password, score, criteria)
            
            # Ask to continue
            print(f"\n{Style.BG_PURPLE}{Style.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Style.RESET}")
            again = input(f"\n{Style.BOLD}Test another password? (y/n): {Style.RESET}").lower()
            if again != 'y':
                print(f"\n{Style.BG_GREEN}{Style.BLACK}{Style.BOLD}👋 THANK YOU FOR USING PASSWORD TASTER! 👋{Style.RESET}")
                print(f"{Style.BG_CYAN}{Style.BLACK}{Style.BOLD}🔐 Stay Secure! - Abdullah 🔐{Style.RESET}\n")
                break
                
    except KeyboardInterrupt:
        print(f"\n\n{Style.BG_YELLOW}{Style.BLACK}⚠️ Program interrupted by user ⚠️{Style.RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
