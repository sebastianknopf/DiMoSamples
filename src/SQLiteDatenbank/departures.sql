SELECT
	routes.route_short_name,
	trips.trip_headsign,
	stop_times.departure_time
FROM
	stop_times
LEFT JOIN
	trips ON trips.trip_id = stop_times.trip_id
LEFT JOIN
	routes ON routes.route_id = trips.route_id
WHERE
	stop_id LIKE :stop_id
	AND departure_time > :departure_time
	AND service_id IN (
		SELECT 
			service_id
		FROM
			calendar
		WHERE 
			{dayname} = '1'
		UNION
		SELECT
			service_id
		FROM
			calendar_dates
		WHERE
			calendar_dates.date = :current_date
			AND calendar_dates.exception_type = 1
		EXCEPT
		SELECT
			service_id
		FROM
			calendar_dates
		WHERE
			calendar_dates.date = :current_date
			AND calendar_dates.exception_type = 2
	)
ORDER BY
	departure_time
LIMIT 5