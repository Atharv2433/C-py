using System;
using System.Diagnostics;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Input array from user
            Console.WriteLine("Enter the array elements separated by space:");
            string input = Console.ReadLine();  
            string[] inputs = input.Split(' ');  

            
            int[] array = new int[inputs.Length];
            for (int i = 0; i < inputs.Length; i++)
            {
                array[i] = int.Parse(inputs[i]); 
            }

            
            string argsToPass = string.Join(" ", array);

            // Call the Python script using Process
            Process process = new Process();
            process.StartInfo.FileName = "python3"; 
            process.StartInfo.Arguments = $"/Users/atharv2433/Desktop/MyApp/double_array_with_pymesh.py {argsToPass}";  
            process.StartInfo.RedirectStandardOutput = true;  
            process.StartInfo.RedirectStandardError = true;   
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;

            
            process.Start();

            
            string result = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            
            process.WaitForExit();

            if (!string.IsNullOrEmpty(error))
            {
                Console.WriteLine($"Error from Python script: {error}");
            }
            else
            {
                Console.WriteLine($"Doubled Array (from Python script): {result}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
