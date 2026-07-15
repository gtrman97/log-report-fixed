Read the Apache-style access log at /app/access.log and write a summary report to /app/report.json.

The completed report must satisfy these success criteria:

1. /app/report.json is a valid JSON object containing exactly three keys:
   - "total_requests" (integer)
   - "unique_ips" (integer)
   - "top_path" (string)

2. "total_requests" equals the total number of non-empty entries in /app/access.log.

3. "unique_ips" equals the number of distinct client IP addresses appearing in /app/access.log.

4. "top_path" equals the request path that appears most frequently in /app/access.log.

You have 120 seconds to complete this task.
Do not cheat by using online solutions or hints specific to this task.