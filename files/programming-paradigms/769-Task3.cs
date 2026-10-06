using System;

class Task3
{
    static void Main()
    {
        int n = 4;

        int[,] x = {
            {0, 0, 0, 0},
            {1, 0, 0, 0},
            {0, 2, 0, 0},
            {3, 4, 5, 6}
        };

        bool found = false;

        for (int i = 0; i < n; i++)
        {
            bool allZero = true;

            for (int j = 0; j < n; j++)
            {
                if (x[i, j] != 0)
                {
                    allZero = false;
                    break;
                }
            }

            if (allZero)
            {
                Console.WriteLine("First all-zero row is: " + i);
                found = true;
                break;
            }
        }

        if (!found)
        {
            Console.WriteLine("No all-zero row found.");
        }
    }
}