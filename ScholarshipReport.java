import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class ScholarshipReport {
    static class Student {
        double gpa;
        String major;

        Student(double gpa, String major) {
            this.gpa = gpa;
            this.major = major;
        }
    }

    public static void main(String[] args) throws IOException {
        Map<String, Student> students = new LinkedHashMap<>();

        // Read all lines from the CSV file
        List<String> lines = Files.readAllLines(Paths.get("students.csv"));

        // Start at 1 to skip the CSV header
        for (int i = 1; i < lines.size(); i++) {
            String line = lines.get(i);

            if (!line.trim().isEmpty()) {
                String[] data = line.split(",");

                String name = data[0].trim();
                double gpa = Double.parseDouble(data[1].trim());
                String major = data[2].trim();

                students.put(name, new Student(gpa, major));
            }
        }

        // Calculate and print the average GPA
        double totalGpa = 0;

        for (Student student : students.values()) {
            totalGpa = totalGpa + student.gpa;
        }

        double averageGpa = totalGpa / students.size();
        System.out.printf("Average GPA: %.2f%n", averageGpa);

        // Print students whose GPA is above average
        System.out.println("\nAbove-average students:");

        for (Map.Entry<String, Student> entry : students.entrySet()) {
            Student student = entry.getValue();

            if (student.gpa > averageGpa) {
                System.out.printf("%s: %.2f%n", entry.getKey(), student.gpa);
            }
        }

        // Predict scholarship eligibility using the major and GPA rules
        System.out.println("\nPredicted scholarship recipients:");

        for (Map.Entry<String, Student> entry : students.entrySet()) {
            String name = entry.getKey();
            Student student = entry.getValue();

            if (student.major.equals("Math") && student.gpa >= 3.50) {
                System.out.printf("%s: %.2f, %s%n",
                        name, student.gpa, student.major);
            } else if (student.major.equals("Biology")
                    && student.gpa >= 2.75) {
                System.out.printf("%s: %.2f, %s%n",
                        name, student.gpa, student.major);
            }
        }
    }
}