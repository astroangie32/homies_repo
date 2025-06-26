# warrior_cli_gui.py

import argparse
from scaffold_core import WarriorMemoryScaffold
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext


def launch_cli():
    parser = argparse.ArgumentParser(description="Warrior Intelligence Core CLI")
    parser.add_argument('--theme', help='Search by theme')
    parser.add_argument('--text', help='Search by text')
    parser.add_argument('--rank', help='Rank entries by similarity to input query')
    parser.add_argument('--json', default='warrior_crystallized_intelligence_module.json', help='Path to memory JSON')
    args = parser.parse_args()

    scaffold = WarriorMemoryScaffold(args.json)

    if args.theme:
        print("🔍 Theme Matches:")
        for entry in scaffold.search_by_theme(args.theme):
            print(f"- {entry.get('title')} [{entry.get('theme')}]")

    if args.text:
        print("🔍 Text Matches:")
        for entry in scaffold.search_by_text(args.text):
            print(f"- {entry.get('title')} :: {entry.get('text')[:100]}...")

    if args.rank:
        print("📊 Top Matches by Similarity:")
        for entry in scaffold.rank_by_similarity(args.rank):
            print(f"- {entry.get('title')} :: {entry.get('text')[:100]}...")


def launch_gui():
    scaffold = WarriorMemoryScaffold("warrior_crystallized_intelligence_module.json")

    def show_results(results):
        result_window = tk.Toplevel()
        result_window.title("Results")
        result_text = scrolledtext.ScrolledText(result_window, width=100, height=30)
        result_text.pack(padx=10, pady=10)
        for r in results:
            result_text.insert(tk.END, f"Title: {r.get('title')}\nTheme: {r.get('theme')}\nText: {r.get('text')[:300]}...\n\n")
        result_text.config(state=tk.DISABLED)

    def do_theme():
        term = simpledialog.askstring("Search by Theme", "Enter theme keyword:")
        if term:
            show_results(scaffold.search_by_theme(term))

    def do_text():
        term = simpledialog.askstring("Search by Text", "Enter text keyword:")
        if term:
            show_results(scaffold.search_by_text(term))

    def do_rank():
        query = simpledialog.askstring("Rank Similarity", "Enter query string:")
        if query:
            show_results(scaffold.rank_by_similarity(query))

    root = tk.Tk()
    root.title("🧠 Warrior Intelligence Core GUI")

    tk.Button(root, text="Search by Theme", width=30, command=do_theme).pack(pady=5)
    tk.Button(root, text="Search by Text", width=30, command=do_text).pack(pady=5)
    tk.Button(root, text="Rank by Similarity", width=30, command=do_rank).pack(pady=5)
    tk.Button(root, text="Exit", width=30, command=root.destroy).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        launch_cli()
    else:
        launch_gui()
