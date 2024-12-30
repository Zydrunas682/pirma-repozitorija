# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "data": {
#       "text/plain": [
#        "4"
#       ]
#      },
#      "execution_count": 1,
#      "metadata": {},
#      "output_type": "execute_result"
#     }
#    ],
#    "source": [
#     "2+2"
#    ]
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.13.0"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 2
# }

import requests

data = requests.get("https://www.skelbimai.lt/skelbimas/2-kambariu-nuoma-8096286")

print(data.status_code)






