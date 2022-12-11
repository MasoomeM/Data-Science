{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Lists\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "B=[\"a\",\"b\",\"c\"]\n",
    "my_family = [\"liz\" , 1.73, \"emma\", 1.68, \"mom\", 1.71, \"dad\", 1.89]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.68"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_family[3]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B[0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_family[0:2] = [\"lisa\", 1.74]\n",
    "my_family"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['A', 'b', 'c']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'c'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "B[0]=B[0].upper()\n",
    "print(B)\n",
    "B[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Dictionaries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Thriller': '1982',\n",
       " 'Back in Black': '1980',\n",
       " 'The Dark Side of the Moon': '1973',\n",
       " 'The Bodyguard': '1992',\n",
       " 'Bat Out of Hell': '1977',\n",
       " 'Their Greatest Hits (1971-1975)': '1976',\n",
       " 'Saturday Night Fever': '1977',\n",
       " 'Rumours': '1977'}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict = {\"Thriller\": \"1982\", \"Back in Black\": \"1980\", \\\n",
    "                    \"The Dark Side of the Moon\": \"1973\", \"The Bodyguard\": \"1992\", \\\n",
    "                    \"Bat Out of Hell\": \"1977\", \"Their Greatest Hits (1971-1975)\": \"1976\", \\\n",
    "                    \"Saturday Night Fever\": \"1977\", \"Rumours\": \"1977\"}\n",
    "release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1982'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict['Thriller'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1992'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict['The Bodyguard'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict.keys() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict.values() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Thriller': '1982',\n",
       " 'Back in Black': '1980',\n",
       " 'The Dark Side of the Moon': '1973',\n",
       " 'The Bodyguard': '1992',\n",
       " 'Bat Out of Hell': '1977',\n",
       " 'Their Greatest Hits (1971-1975)': '1976',\n",
       " 'Saturday Night Fever': '1977',\n",
       " 'Rumours': '1977',\n",
       " 'Graduation': '2007'}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "release_year_dict['Graduation'] = '2007'\n",
    "release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Back in Black': '1980',\n",
       " 'The Dark Side of the Moon': '1973',\n",
       " 'The Bodyguard': '1992',\n",
       " 'Bat Out of Hell': '1977',\n",
       " 'Their Greatest Hits (1971-1975)': '1976',\n",
       " 'Saturday Night Fever': '1977',\n",
       " 'Rumours': '1977'}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del(release_year_dict['Thriller'])\n",
    "del(release_year_dict['Graduation'])\n",
    "release_year_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Verify the key is in the dictionary\n",
    "\n",
    "'The Bodyguard' in release_year_dict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " ## Class in python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Car(object):\n",
    "    def __init__(self,make,model,color):\n",
    "        self.make=make;\n",
    "        self.model=model;\n",
    "        self.color=color;\n",
    "        self.owner_number=0 \n",
    "    def car_info(self):\n",
    "        print(\"make: \",self.make)\n",
    "        print(\"model:\", self.model)\n",
    "        print(\"color:\",self.color)\n",
    "        print(\"number of owners:\",self.owner_number)\n",
    "    def sell(self):\n",
    "        self.owner_number=self.owner_number+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#  Create a Car object\n",
    "make=\"BMW\"\n",
    "model=\"M3\"\n",
    "color=\"red\"\n",
    "#my_car = Car(make=\"BMW\",model=\"M3\",color=\"red\")\n",
    "my_car = Car(\"BMW\",\"M2\",\"red\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "make:  BMW\n",
      "model: M2\n",
      "color: red\n",
      "number of owners: 0\n"
     ]
    }
   ],
   "source": [
    "#  Data Attributes\n",
    "my_car.car_info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "make:  BMW\n",
      "model: M2\n",
      "color: red\n",
      "number of owners: 5\n"
     ]
    }
   ],
   "source": [
    "# Method\n",
    "for i in range(5):\n",
    "    my_car.sell()    \n",
    "my_car.car_info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
