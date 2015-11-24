import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class TimeAngleProblem {
	public static void main(String[] args) {

		if (args.length != 1) {
			System.out.println("Please run with 1 argument - a time value in the format HH:MM");
			return;
		}
		else {
			Pattern pattern = Pattern.compile("\\d\\d:[0-5]\\d");
			Matcher matcher = pattern.matcher(args[0]);
			if (!matcher.matches()) {
				System.out.println("Please check your time value format HH:MM");
				return;
			}
		}

		String[] splitter = args[0].split(":");
		int hour = Integer.parseInt(splitter[0]);
		int minutes = Integer.parseInt(splitter[1]);

		double difference = Math.abs(calculateHourAngle(hour, minutes) - calculateMinutesAngle(minutes));
		difference = difference == 180 ? 180 : difference % 180;

		System.out.println("The angle difference between the hour and minute hand at time " + args[0] + " is " + difference + " degrees");
	}

	private static double calculateHourAngle(int hour, int minutes) {
		double hourComponent = (hour % 12) * 30;
		double minutesComponent = minutes / 2.0;
		return hourComponent + minutesComponent;
	}

	private static double calculateMinutesAngle(int minutes) {
		return 6 * minutes;
	}
}
