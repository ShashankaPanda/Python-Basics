{
  "nbformat": 4,
  "nbformat_minor": 0,
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
      "version": "3.6.8"
    },
    "colab": {
      "name": "1.Python Assignment.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShashankaPanda/Python-Basics/blob/main/1_Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "l0ZzOlyxB-kf"
      },
      "source": [
        "<h1>Python: without numpy or sklearn </h1>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C0xO8JV9B-ki"
      },
      "source": [
        "<h3> Q1: Given two matrices please print the product of those two matrices </h3>\n",
        "<pre>\n",
        "\n",
        "Ex 1: A   = [[1 3 4]\n",
        "             [2 5 7]\n",
        "             [5 9 6]]\n",
        "      B   = [[1 0 0]\n",
        "             [0 1 0]\n",
        "             [0 0 1]]\n",
        "      A*B = [[1 3 4]\n",
        "             [2 5 7]\n",
        "             [5 9 6]]\n",
        "\n",
        "     \n",
        "Ex 2: A   = [[1 2]\n",
        "             [3 4]]\n",
        "      B   = [[1 2 3 4 5]\n",
        "             [5 6 7 8 9]]\n",
        "      A*B = [[11 14 17 20 23]\n",
        "             [23 30 36 42 51]]\n",
        "             \n",
        "Ex 3: A   = [[1 2]\n",
        "             [3 4]]\n",
        "      B   = [[1 4]\n",
        "             [5 6]\n",
        "             [7 8]\n",
        "             [9 6]]\n",
        "      A*B =Not possible\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tjODKUvoQepi"
      },
      "source": [
        "A = [[1,3,4],\n",
        "     [2,5,7],\n",
        "     [5,9,6]]\n",
        "\n",
        "B=  [[1,0,0],\n",
        "    [0,1,0],\n",
        "    [0,0,1]]\n",
        "\n",
        "C = [[1,2,3,4,5,6],\n",
        "     [7,8,9,10,11,12]]  \n",
        "\n",
        "D = [[1,2],\n",
        "     [3,4]] "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rnssAfpgB-kj",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "13c6fddb-daf0-4dc1-f008-d1cd745a7d3d"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input examples\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "# here A and B are list of lists\n",
        "def matrix_mul(A, B):\n",
        "  \n",
        "  if len(A[0]) != len(B):\n",
        "    print('Matrix Multiplication cannot be done')\n",
        "  else:\n",
        "    result = [([0]*len(B[0])) for i in range(len(A))]\n",
        "    for rowindex in range(len(A)):\n",
        "      for colindex in range(len(B[0])):\n",
        "        sum=0\n",
        "        for j in range(len(A[0])):\n",
        "          sum=sum + A[rowindex][j]*B[j][colindex]\n",
        "        result[rowindex][colindex]=sum\n",
        "    return(result)\n",
        "\n",
        "matrix_mul(D, C)\n",
        "\n",
        "#Reference for creating zero matrix - https://stackoverflow.com/questions/54964557/how-to-create-a-zero-matrix-without-using-numpy"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[15, 18, 21, 24, 27, 30], [31, 38, 45, 52, 59, 66]]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "at4VwLggB-kn"
      },
      "source": [
        "<h3> Q2: Select a number randomly with probability proportional to its magnitude from the given array of n elements</h3>\n",
        "\n",
        "consider an experiment, selecting an element from the list A randomly with probability proportional to its magnitude.\n",
        "assume we are doing the same experiment for 100 times with replacement, in each experiment you will print a number that is selected randomly from A.\n",
        "\n",
        "<pre>\n",
        "Ex 1: A = [0 5 27 6 13 28 100 45 10 79]\n",
        "let f(x) denote the number of times x getting selected in 100 experiments.\n",
        "f(100) > f(79) > f(45) > f(28) > f(27) > f(13) > f(10) > f(6) > f(5) > f(0)\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B6S2dpBhB-kn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "82a391ed-68af-4f53-eae0-a318e70198fe"
      },
      "source": [
        "from random import uniform\n",
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input examples\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def pick_a_number_from_list(A):\n",
        "    sum=0\n",
        "    avg=[]\n",
        "    avgsum=0\n",
        "    sumarr=[]\n",
        "    output=[]\n",
        "    A.sort()\n",
        "    for x in range(len(A)):\n",
        "      sum += A[x]\n",
        "    for y in range(len(A)):\n",
        "      avg.append(A[y]/sum)\n",
        "    print(avg)\n",
        "    for z in range(len(A)):\n",
        "      avgsum=avgsum+avg[z]\n",
        "      sumarr.append(avgsum)\n",
        "    print(sumarr)\n",
        "    \n",
        "    for p in range(1,100):\n",
        "      rand = uniform(0.0,1.0)\n",
        "      copysumarr=[]\n",
        "      copysumarr=list(sumarr)\n",
        "      copysumarr.append(rand)\n",
        "      copysumarr.sort()\n",
        "      index1=copysumarr.index(rand)\n",
        "      output.append(A[index1])\n",
        "    \n",
        "    return output #selected_random_number\n",
        "\n",
        "def sampling_based_on_magnitued():\n",
        "  A = [1,5,27,6,13,28,100,45,10,79,23]\n",
        " #   for i in range(1,100):\n",
        "  number = pick_a_number_from_list(A)\n",
        "  print(number)\n",
        "\n",
        "sampling_based_on_magnitued()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0.002967359050445104, 0.01483679525222552, 0.017804154302670624, 0.02967359050445104, 0.03857566765578635, 0.06824925816023739, 0.08011869436201781, 0.0830860534124629, 0.13353115727002968, 0.2344213649851632, 0.29673590504451036]\n",
            "[0.002967359050445104, 0.017804154302670624, 0.03560830860534125, 0.06528189910979229, 0.10385756676557864, 0.17210682492581603, 0.2522255192878338, 0.3353115727002967, 0.4688427299703264, 0.7032640949554896, 1.0]\n",
            "[100, 27, 45, 79, 23, 27, 79, 28, 79, 28, 79, 23, 45, 28, 100, 79, 28, 100, 79, 23, 45, 100, 79, 79, 79, 100, 23, 79, 79, 79, 79, 45, 1, 79, 28, 100, 79, 13, 100, 27, 100, 100, 28, 100, 27, 45, 79, 100, 100, 27, 1, 23, 28, 27, 100, 79, 100, 45, 45, 79, 27, 79, 100, 45, 100, 23, 79, 79, 100, 100, 79, 100, 100, 79, 28, 79, 100, 100, 6, 100, 27, 28, 100, 79, 100, 100, 10, 100, 13, 23, 100, 100, 28, 79, 79, 45, 45, 23, 100]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "D1xQy2WWB-kq"
      },
      "source": [
        "<h3> Q3: Replace the digits in the string with #</h3>\n",
        "\n",
        "consider a string that will have digits in that, we need to remove all the not digits and replace the digits with #\n",
        "<pre>\n",
        "Ex 1: A = 234                Output: ###\n",
        "Ex 2: A = a2b3c4             Output: ###\n",
        "Ex 3: A = abc                Output:   (empty string)\n",
        "Ex 5: A = #2a$#b%c%561#      Output: ####\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fxczi2jzB-kr",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 37
        },
        "outputId": "50ad43e0-26db-4c05-db8f-4a46b8271710"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input examples\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "# String: it will be the input to your program\n",
        "def split(String):\n",
        "  return [char for char in String]\n",
        "\n",
        "def replace_digits(String):\n",
        "  wordlist=split(String)\n",
        "  wordlist2=[]\n",
        "  j = sum(1 for x in wordlist for c in x if c.isdigit())\n",
        "  if (j>0):\n",
        "    for i in range (0,j):\n",
        "      wordlist2.append('#')\n",
        "  else:\n",
        "    wordlist2.clear()\n",
        "  updatedlist=\"\".join(wordlist2)\n",
        "  return updatedlist # modified string which is after replacing the # with digits\n",
        "\n",
        "String=\"#2a$#b%c%561#\" \n",
        "replace_digits(String)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'####'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j7h0Ywg7B-kw"
      },
      "source": [
        "<h3> Q4: Students marks dashboard</h3>\n",
        "\n",
        "consider the marks list of class students given two lists <br>\n",
        "Students = ['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] <br>\n",
        "Marks = [45, 78, 12, 14, 48, 43, 45, 98, 35, 80] <br>\n",
        "from the above two lists the Student[0] got Marks[0],  Student[1] got Marks[1] and so on <br><br>\n",
        "your task is to print the name of students\n",
        "<strong>a. Who got top 5 ranks, in the descending order of marks</strong> <br>\n",
        "<strong>b. Who got least 5 ranks, in the increasing order of marks</strong><br>\n",
        "<strong>d. Who got marks between  &gt;25th percentile &lt;75th percentile, in the increasing order of marks</strong>\n",
        "\n",
        "<pre>\n",
        "Ex 1: \n",
        "Students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] \n",
        "Marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]\n",
        "a. \n",
        "student8  98\n",
        "student10 80\n",
        "student2  78\n",
        "student5  48\n",
        "student7  47\n",
        "b.\n",
        "student3 12\n",
        "student4 14\n",
        "student9 35\n",
        "student6 43\n",
        "student1 45\n",
        "c.\n",
        "student9 35\n",
        "student6 43\n",
        "student1 45\n",
        "student7 47\n",
        "student5 48\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cxPJgItsB-kx",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e337b48-b842-47e6-d786-1641496cbb6e"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input examples\n",
        "\n",
        "import math\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def display_dash_board(students, marks):\n",
        "    \n",
        "    # write code for computing top top 5 students\n",
        "    top_5_students = (sorted(zip(marks,students),reverse=True))[:5]\n",
        "    \n",
        "    # write code for computing top least 5 students\n",
        "    least_5_students = (sorted(zip(marks,students)))[:-5]\n",
        "    \n",
        "    # write code for computing top least 5 students\n",
        "    sortedstudents2= [x for y, x in sorted(zip(marks,students))]\n",
        "    s = len(sortedstudents2)\n",
        "    i= sorted(zip(marks,students))[int(math.ceil((s * 25) / 100)) - 1][1]\n",
        "    j= sorted(zip(marks,students))[int(math.ceil((s * 75) / 100)) - 1][1]\n",
        "    students_within_25_and_75 = (sorted(zip(marks,students)))[sortedstudents2.index(i):sortedstudents2.index(j)]\n",
        "    \n",
        "    return top_5_students, least_5_students, students_within_25_and_75\n",
        "\n",
        "\n",
        "students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] \n",
        "marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]\n",
        "\n",
        "top_5_students, least_5_students, students_within_25_and_75 = display_dash_board(students, marks)\n",
        "\n",
        "print('a.')\n",
        "for a in range (0,len(top_5_students)):\n",
        "  print(top_5_students[a][1],top_5_students[a][0])\n",
        "print('b.')\n",
        "for a in range (0,len(least_5_students)):\n",
        "  print(least_5_students[a][1],least_5_students[a][0])\n",
        "print('c.')\n",
        "for a in range (0,len(students_within_25_and_75)):\n",
        "  print(students_within_25_and_75[a][1],students_within_25_and_75[a][0])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "a.\n",
            "student8 98\n",
            "student10 80\n",
            "student2 78\n",
            "student5 48\n",
            "student7 47\n",
            "b.\n",
            "student3 12\n",
            "student4 14\n",
            "student9 35\n",
            "student6 43\n",
            "student1 45\n",
            "c.\n",
            "student9 35\n",
            "student6 43\n",
            "student1 45\n",
            "student7 47\n",
            "student5 48\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qha0OhQHB-k1"
      },
      "source": [
        "<h3> Q5: Find the closest points</h3>\n",
        "\n",
        "consider you have given n data points in the form of list of tuples like S=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),..,(xn,yn)] and a point P=(p,q) <br> your task is to find 5 closest points(based on cosine distance) in S from P\n",
        "<br>cosine distance between two points (x,y) and (p,q) is defind as $cos^{-1}(\\frac{(x\\cdot p+y\\cdot q)}{\\sqrt(x^2+y^2)\\cdot\\sqrt(p^2+q^2)})$\n",
        "<pre>\n",
        "Ex:\n",
        "\n",
        "S= [(1,2),(3,4),(-1,1),(6,-7),(0, 6),(-5,-8),(-1,-1)(6,0),(1,-1)]\n",
        "P= (3,-4)\n",
        "<img src='https://i.imgur.com/vIFPOcG.jpg', width=300>\n",
        "Output:\n",
        "(6,-7)\n",
        "(1,-1)\n",
        "(6,0)\n",
        "(-5,-8)\n",
        "(-1,-1)\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wA5I1g-2B-k2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e5e8ce55-c8da-4ad3-a4a9-554dffed5764"
      },
      "source": [
        "import math\n",
        "\n",
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input examples\n",
        "# you can free to change all these codes/structure\n",
        "\n",
        "dist= []\n",
        "# here S is list of tuples and P is a tuple ot len=2\n",
        "def closest_points_to_p(S, P):\n",
        "    for i in range(len(S)):\n",
        "      d = math.acos(((S[i][0]*P[0])+(S[i][1]*P[1]))/((math.sqrt((S[i][0]**2)+(S[i][1]**2))) *(math.sqrt((P[0]**2)+(P[1]**2)))))\n",
        "      dist.append(d)\n",
        "    x = sorted(zip(dist,S))\n",
        "    return x\n",
        "\n",
        "\n",
        "S=[(1,2),(3,4),(-1,1),(6,-7),(0,6),(-5,-8),(-1,-1),(6,0),(1,-1)]\n",
        "P=(3,-4)\n",
        "points = closest_points_to_p(S, P)\n",
        "for x in range (0,5):\n",
        "  print('Coordinate:',points[x][1],', distance:',points[x][0]) #print the returned values"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Coordinate: (6, -7) , distance: 0.06512516333438509\n",
            "Coordinate: (1, -1) , distance: 0.14189705460416438\n",
            "Coordinate: (6, 0) , distance: 0.9272952180016123\n",
            "Coordinate: (-5, -8) , distance: 1.2021004241368467\n",
            "Coordinate: (-1, -1) , distance: 1.4288992721907328\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-g11jeAiB-k5"
      },
      "source": [
        "<h3> Q6: Find Which line separates oranges and apples</h3>\n",
        "consider you have given two set of data points in the form of list of tuples like \n",
        "<pre>\n",
        "Red =[(R11,R12),(R21,R22),(R31,R32),(R41,R42),(R51,R52),..,(Rn1,Rn2)]\n",
        "Blue=[(B11,B12),(B21,B22),(B31,B32),(B41,B42),(B51,B52),..,(Bm1,Bm2)]\n",
        "</pre>\n",
        "and set of line equations(in the string formate, i.e list of strings)\n",
        "<pre>\n",
        "Lines = [a1x+b1y+c1,a2x+b2y+c2,a3x+b3y+c3,a4x+b4y+c4,..,K lines]\n",
        "Note: you need to string parsing here and get the coefficients of x,y and intercept\n",
        "</pre>\n",
        "your task is to for each line that is given print \"YES\"/\"NO\", you will print yes, if all the red points are one side of the line and blue points are other side of the line, otherwise no\n",
        "<pre>\n",
        "Ex:\n",
        "Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]\n",
        "Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]\n",
        "Lines=[\"1x+1y+0\",\"1x-1y+0\",\"1x+0y-3\",\"0x+1y-0.5\"]\n",
        "<img src='https://i.imgur.com/DoQf7mE.jpg' width=400>\n",
        "Output:\n",
        "YES\n",
        "NO\n",
        "NO\n",
        "YES\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eRxExaTRB-k6"
      },
      "source": [
        "import math\n",
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input strings\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def i_am_the_one(red,blue,line):\n",
        "    # your code\n",
        "    return #yes/no\n",
        "\n",
        "Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]\n",
        "Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]\n",
        "Lines=[\"1x+1y+0\",\"1x-1y+0\",\"1x+0y-3\",\"0x+1y-0.5\"]\n",
        "\n",
        "for i in Lines:\n",
        "    yes_or_no = i_am_the_one(Red, Blue, i)\n",
        "    print() # the returned value"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9OBpURbNB-k9"
      },
      "source": [
        "<h3> Q7: Filling the missing values in the specified formate</h3>\n",
        "You will be given a string with digits and '\\_'(missing value) symbols you have to replace the '\\_' symbols as explained \n",
        "<pre>\n",
        "Ex 1: _, _, _, 24 ==> 24/4, 24/4, 24/4, 24/4 i.e we. have distributed the 24 equally to all 4 places <br>\n",
        "Ex 2: 40, _, _, _, 60 ==> (60+40)/5,(60+40)/5,(60+40)/5,(60+40)/5,(60+40)/5 ==> 20, 20, 20, 20, 20 i.e. the sum of (60+40) is distributed qually to all 5 places<br>\n",
        "Ex 3: 80, _, _, _, _  ==> 80/5,80/5,80/5,80/5,80/5 ==> 16, 16, 16, 16, 16 i.e. the 80 is distributed qually to all 5 missing values that are right to it<br>\n",
        "Ex 4: _, _, 30, _, _, _, 50, _, _  \n",
        "==> we will fill the missing values from left to right \n",
        "    a. first we will distribute the 30 to left two missing values (10, 10, 10, _, _, _, 50, _, _)\n",
        "    b. now distribute the sum (10+50) missing values in between (10, 10, 12, 12, 12, 12, 12, _, _) \n",
        "    c. now we will distribute 12 to right side missing values (10, 10, 12, 12, 12, 12, 4, 4, 4)\n",
        "</pre>\n",
        "for a given string with comma seprate values, which will have both missing values numbers like ex: \"_, _, x, _, _, _\"\n",
        "you need fill the missing values\n",
        "\n",
        "Q: your program reads a string like ex: \"_, _, x, _, _, _\" and returns the filled sequence\n",
        "\n",
        "Ex: \n",
        "<pre>\n",
        "Input1: \"_,_,_,24\"\n",
        "Output1: 6,6,6,6\n",
        "\n",
        "Input2: \"40,_,_,_,60\"\n",
        "Output2: 20,20,20,20,20\n",
        "\n",
        "Input3: \"80,_,_,_,_\"\n",
        "Output3: 16,16,16,16,16\n",
        "\n",
        "Input4: \"_,_,30,_,_,_,50,_,_\"\n",
        "Output4: 10,10,12,12,12,12,4,4,4\n",
        "</pre>\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nZmpzHs_B-k-"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input strings\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def curve_smoothing(string):\n",
        "    # your code\n",
        "    return #list of values\n",
        "\n",
        "S=  \"_,_,30,_,_,_,50,_,_\"\n",
        "smoothed_values= curve_smoothing(S)\n",
        "print(# print above values)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RBz4pzlfB-lB"
      },
      "source": [
        "<h3> Q8: Filling the missing values in the specified formate</h3>\n",
        "You will be given a list of lists, each sublist will be of length 2 i.e. [[x,y],[p,q],[l,m]..[r,s]]\n",
        "consider its like a martrix of n rows and two columns\n",
        "1. the first column F will contain only 5 uniques values (F1, F2, F3, F4, F5)\n",
        "2. the second column S will contain only 3 uniques values (S1, S2, S3)\n",
        "<pre>\n",
        "your task is to find\n",
        "a. Probability of P(F=F1|S==S1), P(F=F1|S==S2), P(F=F1|S==S3)\n",
        "b. Probability of P(F=F2|S==S1), P(F=F2|S==S2), P(F=F2|S==S3)\n",
        "c. Probability of P(F=F3|S==S1), P(F=F3|S==S2), P(F=F3|S==S3)\n",
        "d. Probability of P(F=F4|S==S1), P(F=F4|S==S2), P(F=F4|S==S3)\n",
        "e. Probability of P(F=F5|S==S1), P(F=F5|S==S2), P(F=F5|S==S3)\n",
        "</pre>\n",
        "Ex:\n",
        "\n",
        "<pre>\n",
        "[[F1,S1],[F2,S2],[F3,S3],[F1,S2],[F2,S3],[F3,S2],[F2,S1],[F4,S1],[F4,S3],[F5,S1]]\n",
        "\n",
        "a. P(F=F1|S==S1)=1/4, P(F=F1|S==S2)=1/3, P(F=F1|S==S3)=0/3\n",
        "b. P(F=F2|S==S1)=1/4, P(F=F2|S==S2)=1/3, P(F=F2|S==S3)=1/3\n",
        "c. P(F=F3|S==S1)=0/4, P(F=F3|S==S2)=1/3, P(F=F3|S==S3)=1/3\n",
        "d. P(F=F4|S==S1)=1/4, P(F=F4|S==S2)=0/3, P(F=F4|S==S3)=1/3\n",
        "e. P(F=F5|S==S1)=1/4, P(F=F5|S==S2)=0/3, P(F=F5|S==S3)=0/3\n",
        "</pre>\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e-1giz1MB-lC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8b116fef-9207-4062-8e4f-274efcba1401"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input strings\n",
        "\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "\n",
        "from fractions import Fraction\n",
        "\n",
        "def compute_conditional_probabilites(A):\n",
        "    for i in range(len(A)):\n",
        "      if(A[i][0]=='F1' and A[i][1]=='S1'):\n",
        "        FSCombinationDictionary['F1S1'] =  FSCombinationDictionary['F1S1']+1\n",
        "        SDictionary['S1'] = SDictionary['S1']+1\n",
        "      if(A[i][0]=='F1' and A[i][1]=='S2'):\n",
        "        FSCombinationDictionary['F1S2'] =  FSCombinationDictionary['F1S2']+1\n",
        "        SDictionary['S2'] = SDictionary['S2']+1\n",
        "      if(A[i][0]=='F1' and A[i][1]=='S3'):\n",
        "        FSCombinationDictionary['F1S3'] =  FSCombinationDictionary['F1S3']+1\n",
        "        SDictionary['S3'] = SDictionary['S3']+1\n",
        "      if(A[i][0]=='F2' and A[i][1]=='S1'):\n",
        "        FSCombinationDictionary['F2S1'] =  FSCombinationDictionary['F2S1']+1\n",
        "        SDictionary['S1'] = SDictionary['S1']+1\n",
        "      if(A[i][0]=='F2' and A[i][1]=='S2'):\n",
        "        FSCombinationDictionary['F2S2'] =  FSCombinationDictionary['F2S2']+1\n",
        "        SDictionary['S2'] = SDictionary['S2']+1\n",
        "      if(A[i][0]=='F2' and A[i][1]=='S3'):\n",
        "        FSCombinationDictionary['F2S3'] =  FSCombinationDictionary['F2S3']+1\n",
        "        SDictionary['S3'] = SDictionary['S3']+1\n",
        "      if(A[i][0]=='F3' and A[i][1]=='S1'):\n",
        "        FSCombinationDictionary['F3S1'] =  FSCombinationDictionary['F3S1']+1\n",
        "        SDictionary['S1'] = SDictionary['S1']+1\n",
        "      if(A[i][0]=='F3' and A[i][1]=='S2'):\n",
        "        FSCombinationDictionary['F3S2'] =  FSCombinationDictionary['F3S2']+1\n",
        "        SDictionary['S2'] = SDictionary['S2']+1\n",
        "      if(A[i][0]=='F3' and A[i][1]=='S3'):\n",
        "        FSCombinationDictionary['F3S3'] =  FSCombinationDictionary['F3S3']+1\n",
        "        SDictionary['S3'] = SDictionary['S3']+1\n",
        "      if(A[i][0]=='F4' and A[i][1]=='S1'):\n",
        "        FSCombinationDictionary['F4S1'] =  FSCombinationDictionary['F4S1']+1\n",
        "        SDictionary['S1'] = SDictionary['S1']+1\n",
        "      if(A[i][0]=='F4' and A[i][1]=='S2'):\n",
        "        FSCombinationDictionary['F4S2'] =  FSCombinationDictionary['F4S2']+1\n",
        "        SDictionary['S2'] = SDictionary['S2']+1\n",
        "      if(A[i][0]=='F4' and A[i][1]=='S3'):\n",
        "        FSCombinationDictionary['F4S3'] =  FSCombinationDictionary['F4S3']+1\n",
        "        SDictionary['S3'] = SDictionary['S3']+1\n",
        "      if(A[i][0]=='F5' and A[i][1]=='S1'):\n",
        "        FSCombinationDictionary['F5S1'] =  FSCombinationDictionary['F5S1']+1\n",
        "        SDictionary['S1'] = SDictionary['S1']+1\n",
        "      if(A[i][0]=='F5' and A[i][1]=='S2'):\n",
        "        FSCombinationDictionary['F5S2'] =  FSCombinationDictionary['F5S2']+1\n",
        "        SDictionary['S2'] = SDictionary['S2']+1\n",
        "      if(A[i][0]=='F5' and A[i][1]=='S3'):\n",
        "        FSCombinationDictionary['F5S3'] =  FSCombinationDictionary['F5S3']+1\n",
        "        SDictionary['S3'] = SDictionary['S3']+1\n",
        "    # print the output as per the instructions\n",
        "\n",
        "A = [['F1','S1'],['F2','S2'],['F3','S3'],['F1','S2'],['F2','S3'],['F3','S2'],['F2','S1'],['F4','S1'],['F4','S3'],['F5','S1']]\n",
        "\n",
        "FSCombinationDictionary = {'F1S1':0,'F1S2':0,'F1S3':0,'F2S1':0,'F2S2':0,'F2S3':0,'F3S1':0,'F3S2':0,'F3S3':0,'F4S1':0,'F4S2':0,'F4S3':0,'F5S1':0,'F5S2':0,'F5S3':0}\n",
        "\n",
        "SDictionary = {'S1':0,'S2':0,'S3':0}\n",
        "\n",
        "compute_conditional_probabilites(A)\n",
        "\n",
        "print('P(F=F1|S==S1) = ',Fraction(FSCombinationDictionary['F1S1']/SDictionary['S1']).limit_denominator())\n",
        "print('P(F=F2|S==S1) = ',Fraction(FSCombinationDictionary['F2S1']/SDictionary['S1']).limit_denominator())\n",
        "print('P(F=F3|S==S1) = ',Fraction(FSCombinationDictionary['F3S1']/SDictionary['S1']).limit_denominator())\n",
        "print('P(F=F4|S==S1) = ',Fraction(FSCombinationDictionary['F4S1']/SDictionary['S1']).limit_denominator())\n",
        "print('P(F=F5|S==S1) = ',Fraction(FSCombinationDictionary['F5S1']/SDictionary['S1']).limit_denominator())\n",
        "print('P(F=F1|S==S2) = ',Fraction(FSCombinationDictionary['F1S2']/SDictionary['S2']).limit_denominator())\n",
        "print('P(F=F2|S==S2) = ',Fraction(FSCombinationDictionary['F2S2']/SDictionary['S2']).limit_denominator())\n",
        "print('P(F=F3|S==S2) = ',Fraction(FSCombinationDictionary['F3S2']/SDictionary['S2']).limit_denominator())\n",
        "print('P(F=F4|S==S2) = ',Fraction(FSCombinationDictionary['F4S2']/SDictionary['S2']).limit_denominator())\n",
        "print('P(F=F5|S==S2) = ',Fraction(FSCombinationDictionary['F5S2']/SDictionary['S2']).limit_denominator())\n",
        "print('P(F=F1|S==S3) = ',Fraction(FSCombinationDictionary['F1S3']/SDictionary['S3']).limit_denominator())\n",
        "print('P(F=F2|S==S3) = ',Fraction(FSCombinationDictionary['F2S3']/SDictionary['S3']).limit_denominator())\n",
        "print('P(F=F3|S==S3) = ',Fraction(FSCombinationDictionary['F3S3']/SDictionary['S3']).limit_denominator())\n",
        "print('P(F=F4|S==S3) = ',Fraction(FSCombinationDictionary['F4S3']/SDictionary['S3']).limit_denominator())\n",
        "print('P(F=F5|S==S3) = ',Fraction(FSCombinationDictionary['F5S3']/SDictionary['S3']).limit_denominator())\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "P(F=F1|S==S1) =  1/4\n",
            "P(F=F2|S==S1) =  1/4\n",
            "P(F=F3|S==S1) =  0\n",
            "P(F=F4|S==S1) =  1/4\n",
            "P(F=F5|S==S1) =  1/4\n",
            "P(F=F1|S==S2) =  1/3\n",
            "P(F=F2|S==S2) =  1/3\n",
            "P(F=F3|S==S2) =  1/3\n",
            "P(F=F4|S==S2) =  0\n",
            "P(F=F5|S==S2) =  0\n",
            "P(F=F1|S==S3) =  0\n",
            "P(F=F2|S==S3) =  1/3\n",
            "P(F=F3|S==S3) =  1/3\n",
            "P(F=F4|S==S3) =  1/3\n",
            "P(F=F5|S==S3) =  0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n4HS87QmB-lF"
      },
      "source": [
        "<h3> Q9: Given two sentances S1, S2</h3>\n",
        "You will be given two sentances S1, S2 your task is to find \n",
        "<pre>\n",
        "a. Number of common words between S1, S2\n",
        "b. Words in S1 but not in S2\n",
        "c. Words in S2 but not in S1\n",
        "</pre>\n",
        "\n",
        "Ex: \n",
        "<pre>\n",
        "S1= \"the first column F will contain only 5 uniques values\"\n",
        "S2= \"the second column S will contain only 3 uniques values\"\n",
        "Output:\n",
        "a. 7\n",
        "b. ['first','F','5']\n",
        "c. ['second','S','3']\n",
        "</pre>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ez7hlHK0B-lG"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input strings\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def string_features(S1, S2):\n",
        "    # your code\n",
        "    return a, b, c\n",
        "\n",
        "S1= \"the first column F will contain only 5 uniques values\"\n",
        "S2= \"the second column S will contain only 3 uniques values\"\n",
        "a,b,c = string_features(S1, S2)\n",
        "print(#the above values)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XefXVEjCB-lI"
      },
      "source": [
        "<h3> Q10: Given two sentances S1, S2</h3>\n",
        "You will be given a list of lists, each sublist will be of length 2 i.e. [[x,y],[p,q],[l,m]..[r,s]]\n",
        "consider its like a martrix of n rows and two columns\n",
        "\n",
        "a. the first column Y will contain interger values <br>\n",
        "b. the second column $Y_{score}$ will be having float values <br>\n",
        "Your task is to find the value of $f(Y,Y_{score}) = -1*\\frac{1}{n}\\Sigma_{for each Y,Y_{score} pair}(Ylog10(Y_{score})+(1-Y)log10(1-Y_{score}))$ here n is the number of rows in the matrix\n",
        "<pre>\n",
        "Ex:\n",
        "[[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]\n",
        "output:\n",
        "0.4243099\n",
        "</pre>\n",
        "$\\frac{-1}{8}\\cdot((1\\cdot log_{10}(0.4)+0\\cdot log_{10}(0.6))+(0\\cdot log_{10}(0.5)+1\\cdot log_{10}(0.5)) + ... + (1\\cdot log_{10}(0.8)+0\\cdot log_{10}(0.2)) )$"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N9zkagyNB-lJ"
      },
      "source": [
        "# write your python code here\n",
        "# you can take the above example as sample input for your program to test\n",
        "# it should work for any general input try not to hard code for only given input strings\n",
        "\n",
        "\n",
        "# you can free to change all these codes/structure\n",
        "def compute_log_loss(A):\n",
        "    # your code\n",
        "    \n",
        "    return loss\n",
        "\n",
        "A = [[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]\n",
        "loss = compute_log_loss(A)\n",
        "print(# the above loss)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}