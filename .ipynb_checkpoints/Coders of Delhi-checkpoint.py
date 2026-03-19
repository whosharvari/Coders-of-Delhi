{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1d1dd14c-e336-4356-acd5-19552bc2547a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fd10d48c-2c72-40f5-bc91-4d8ca5bf5252",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_data(filename):\n",
    "    with open(filename, \"r\") as f:\n",
    "        data = json.load(f)\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c51e6703-9ce5-406e-908e-afb5f486dd52",
   "metadata": {},
   "outputs": [],
   "source": [
    "#load dataset\n",
    "data = load_data(\"/Users/sharvari/Desktop/DS/social-network-recommendation/data/massive_data.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ea53a2e9-d29b-4f05-80a8-bc654f4ce992",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'users': [{'id': 1,\n",
       "   'name': 'Amit',\n",
       "   'friends': [2, 3, 4, 5, 6],\n",
       "   'liked_pages': [101, 102]},\n",
       "  {'id': 2,\n",
       "   'name': 'Priya',\n",
       "   'friends': [1, 3, 5, 6, 7],\n",
       "   'liked_pages': [102, 103]},\n",
       "  {'id': 3,\n",
       "   'name': 'Rahul',\n",
       "   'friends': [1, 2, 4, 7, 8],\n",
       "   'liked_pages': [101, 103]},\n",
       "  {'id': 4, 'name': 'Sara', 'friends': [1, 3, 6, 8, 9], 'liked_pages': [104]},\n",
       "  {'id': 5,\n",
       "   'name': 'Neha',\n",
       "   'friends': [1, 2, 6, 10, 11],\n",
       "   'liked_pages': [102, 105]},\n",
       "  {'id': 6,\n",
       "   'name': 'Vikram',\n",
       "   'friends': [1, 2, 4, 5, 12],\n",
       "   'liked_pages': [106]},\n",
       "  {'id': 7,\n",
       "   'name': 'Kunal',\n",
       "   'friends': [2, 3, 8, 9, 13],\n",
       "   'liked_pages': [101, 107]},\n",
       "  {'id': 8,\n",
       "   'name': 'Anjali',\n",
       "   'friends': [3, 4, 7, 10, 14],\n",
       "   'liked_pages': [103, 108]},\n",
       "  {'id': 9,\n",
       "   'name': 'Ravi',\n",
       "   'friends': [4, 7, 10, 11, 15],\n",
       "   'liked_pages': [104, 109]},\n",
       "  {'id': 10,\n",
       "   'name': 'Sneha',\n",
       "   'friends': [5, 8, 9, 12, 16],\n",
       "   'liked_pages': [110]},\n",
       "  {'id': 11,\n",
       "   'name': 'Arjun',\n",
       "   'friends': [5, 9, 12, 14, 17],\n",
       "   'liked_pages': [105, 111]},\n",
       "  {'id': 12,\n",
       "   'name': 'Meera',\n",
       "   'friends': [6, 10, 11, 13, 18],\n",
       "   'liked_pages': [112]},\n",
       "  {'id': 13,\n",
       "   'name': 'Kabir',\n",
       "   'friends': [7, 12, 14, 15, 19],\n",
       "   'liked_pages': [106, 113]},\n",
       "  {'id': 14,\n",
       "   'name': 'Tanya',\n",
       "   'friends': [8, 11, 13, 16, 20],\n",
       "   'liked_pages': [114]},\n",
       "  {'id': 15,\n",
       "   'name': 'Varun',\n",
       "   'friends': [9, 13, 16, 17, 21],\n",
       "   'liked_pages': [107, 115]},\n",
       "  {'id': 16,\n",
       "   'name': 'Rhea',\n",
       "   'friends': [10, 14, 15, 18, 22],\n",
       "   'liked_pages': [116]},\n",
       "  {'id': 17,\n",
       "   'name': 'Ishan',\n",
       "   'friends': [11, 15, 18, 19, 23],\n",
       "   'liked_pages': [108, 117]},\n",
       "  {'id': 18,\n",
       "   'name': 'Simran',\n",
       "   'friends': [12, 16, 17, 20, 24],\n",
       "   'liked_pages': [118]},\n",
       "  {'id': 19,\n",
       "   'name': 'Pooja',\n",
       "   'friends': [13, 17, 20, 21, 25],\n",
       "   'liked_pages': [109, 119]},\n",
       "  {'id': 20,\n",
       "   'name': 'Yash',\n",
       "   'friends': [14, 18, 19, 22, 26],\n",
       "   'liked_pages': [120]},\n",
       "  {'id': 21,\n",
       "   'name': 'Ananya',\n",
       "   'friends': [15, 19, 22, 23, 27],\n",
       "   'liked_pages': [110, 121]},\n",
       "  {'id': 22,\n",
       "   'name': 'Dev',\n",
       "   'friends': [16, 20, 21, 24, 28],\n",
       "   'liked_pages': [122]},\n",
       "  {'id': 23,\n",
       "   'name': 'Aditi',\n",
       "   'friends': [17, 21, 24, 25, 29],\n",
       "   'liked_pages': [111, 123]},\n",
       "  {'id': 24,\n",
       "   'name': 'Rohan',\n",
       "   'friends': [18, 22, 23, 26, 30],\n",
       "   'liked_pages': [124]},\n",
       "  {'id': 25,\n",
       "   'name': 'Nisha',\n",
       "   'friends': [19, 23, 26, 27, 1],\n",
       "   'liked_pages': [112]},\n",
       "  {'id': 26,\n",
       "   'name': 'Gautam',\n",
       "   'friends': [20, 24, 25, 28, 3],\n",
       "   'liked_pages': [125]},\n",
       "  {'id': 27,\n",
       "   'name': 'Kriti',\n",
       "   'friends': [21, 25, 28, 29, 5],\n",
       "   'liked_pages': [113]},\n",
       "  {'id': 28,\n",
       "   'name': 'Harsh',\n",
       "   'friends': [22, 26, 27, 30, 7],\n",
       "   'liked_pages': [126]},\n",
       "  {'id': 29,\n",
       "   'name': 'Naveen',\n",
       "   'friends': [23, 27, 30, 9, 11],\n",
       "   'liked_pages': [114]},\n",
       "  {'id': 30,\n",
       "   'name': 'Ishita',\n",
       "   'friends': [24, 28, 29, 13, 15],\n",
       "   'liked_pages': [127]}],\n",
       " 'pages': [{'id': 101, 'name': 'Python Developers'},\n",
       "  {'id': 102, 'name': 'Data Science Enthusiasts'},\n",
       "  {'id': 103, 'name': 'AI & ML Community'},\n",
       "  {'id': 104, 'name': 'Web Dev Hub'},\n",
       "  {'id': 105, 'name': 'Blockchain Innovators'},\n",
       "  {'id': 106, 'name': 'Cybersecurity Experts'},\n",
       "  {'id': 107, 'name': 'Cloud Computing Pros'},\n",
       "  {'id': 108, 'name': 'Competitive Programmers'},\n",
       "  {'id': 109, 'name': 'Startup Founders'},\n",
       "  {'id': 110, 'name': 'UI/UX Designers'},\n",
       "  {'id': 111, 'name': 'Full-Stack Developers'},\n",
       "  {'id': 112, 'name': 'Tech Entrepreneurs'},\n",
       "  {'id': 113, 'name': 'IoT Enthusiasts'},\n",
       "  {'id': 114, 'name': 'Game Developers'},\n",
       "  {'id': 115, 'name': 'Big Data Analysts'},\n",
       "  {'id': 116, 'name': 'DevOps Engineers'},\n",
       "  {'id': 117, 'name': 'Cloud AI Researchers'},\n",
       "  {'id': 118, 'name': '5G & Edge Computing'},\n",
       "  {'id': 119, 'name': 'AR/VR Creators'},\n",
       "  {'id': 120, 'name': 'Freelance Coders'},\n",
       "  {'id': 121, 'name': 'Open Source Contributors'},\n",
       "  {'id': 122, 'name': 'Algorithmic Traders'},\n",
       "  {'id': 123, 'name': 'Low-Code Developers'},\n",
       "  {'id': 124, 'name': 'Cyber Ethics Forum'},\n",
       "  {'id': 125, 'name': 'AI Ethics & Policy'},\n",
       "  {'id': 126, 'name': 'Digital Nomads'},\n",
       "  {'id': 127, 'name': 'Women in Tech'}]}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9931cb21-397f-4531-80c2-49c549aa603c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Display users and pages\n",
    "def display_users(data):\n",
    "    print(\"Users and their connections:\")\n",
    "    for user in data['users']:\n",
    "        print(f\"ID:{user['id']} - {user['name']} is friends with: {user['friends']} and liked pages are {user['liked_pages']}\")\n",
    "    print(\"\\nPages Information\")\n",
    "    for page in data['pages']:\n",
    "        print(f\"{page['id']}: {page['name']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "13aaa534-fe1f-4d32-a6ba-615c59e8a87e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data has been cleaned successfully\n"
     ]
    }
   ],
   "source": [
    "# Data cleaning\n",
    "def clean_data(data):\n",
    "    data[\"users\"] = [user for user in data[\"users\"] if user[\"name\"].strip()]\n",
    "    \n",
    "    for user in data[\"users\"]:\n",
    "        user['friends'] = list(set(user['friends']))\n",
    "        \n",
    "    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]\n",
    "\n",
    "    unique_pages = {}\n",
    "    for page in data['pages']:\n",
    "        unique_pages[page['id']] = page\n",
    "    data['pages'] = list(unique_pages.values())\n",
    "    return data\n",
    "    \n",
    "\n",
    "data = clean_data(data)\n",
    "print(\"Data has been cleaned successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "50a27983-8bf2-4211-839b-f1164a7b881b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recommended users for user 10: [11, 6, 4, 7, 14, 15, 18, 1, 2, 3, 13, 22]\n"
     ]
    }
   ],
   "source": [
    "# Friends recommendation\n",
    "def find_people_you_may_know(user_id, data):\n",
    "    user_friends = {}\n",
    "    for user in data['users']:\n",
    "        user_friends[user['id']] = set(user['friends'])\n",
    "        \n",
    "    if user_id not in user_friends:\n",
    "        return []\n",
    "\n",
    "    direct_friends = user_friends[user_id]\n",
    "    suggestions = {}\n",
    "    for friend in direct_friends:\n",
    "        for mutual in user_friends[friend]:\n",
    "            if mutual!=user_id and mutual not in direct_friends:\n",
    "                \n",
    "                suggestions[mutual] = suggestions.get(mutual, 0) + 1\n",
    "    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)   \n",
    "    return [user_id for user_id, mutual_count in sorted_suggestions]\n",
    "\n",
    "user_id = 10\n",
    "recc = find_people_you_may_know(user_id, data)\n",
    "print(f\"Recommended users for user {user_id}: {recc}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5f40c619-6e3a-4a00-a33b-f4db179f1c88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(103, 2), (105, 1), (107, 1), (104, 0), (106, 0), (108, 0), (109, 0), (110, 0), (111, 0), (112, 0), (113, 0), (114, 0), (115, 0), (116, 0), (117, 0), (118, 0), (119, 0), (120, 0), (121, 0), (122, 0), (123, 0), (124, 0), (125, 0), (126, 0), (127, 0)]\n"
     ]
    }
   ],
   "source": [
    "# Page recommendation system\n",
    "def find_pages_you_might_like(user_id, data):\n",
    "    user_pages = {}\n",
    "    \n",
    "    for user in data['users']:\n",
    "        user_pages[user['id']] = set(user['liked_pages'])\n",
    "\n",
    "    if user_id not in user_pages:\n",
    "        return []\n",
    "        \n",
    "    user_liked_pages = user_pages[user_id]\n",
    "    page_suggestion = {}\n",
    "\n",
    "\n",
    "    for other_user, pages in user_pages.items():\n",
    "        if other_user != user_id:\n",
    "            shared_pages = user_liked_pages.intersection(pages)\n",
    "        \n",
    "            for page in pages:\n",
    "                if page not in user_liked_pages:\n",
    "                    page_suggestion[page] = page_suggestion.get(page, 0) + len(shared_pages)\n",
    "\n",
    "    sorted_pages = sorted(page_suggestion.items(), key=lambda x: x[1], reverse=True)\n",
    "    return [(page_id, score) for page_id, score in sorted_pages]\n",
    "\n",
    "user_id = 1\n",
    "page_recommendation = find_pages_you_might_like(user_id, data)\n",
    "print(page_recommendation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c0daac6-6a5f-4169-bc23-49c5b3151064",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
