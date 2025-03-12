{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gangthegoat/git-tutorial/blob/main/hw1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zwFnJsE6vjf8"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def get_radius(prompt) :\n",
        "    r= int(input(prompt))\n",
        "    return r\n",
        "\n",
        "\n",
        "def get_circle_area(radius) :\n",
        "  area= 3.14 * radius * radius\n",
        "  return area\n",
        "\n",
        "input_radius = get_radius('구하고자하는 원의 반지름은?')\n",
        "area = get_circle_area(input_radius)\n",
        "\n",
        "result = f'반지름이 {input_radius}인 원의 넓이= 3.14 x {input_radius} x {input_radius}= {area:.2f}'\n",
        "print(result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NBixbwRKLcUY",
        "outputId": "4f2fdb92-2d99-4b69-a0fa-735dd24dc0d3"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "구하고자하는 원의 반지름은?4\n",
            "반지름이 4인 원의 넓이= 3.14 x 4 x 4= 50.24\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Colaboratory에 오신 것을 환영합니다",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}