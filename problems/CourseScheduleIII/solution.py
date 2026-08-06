import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])
        maxCourses = []
        heapq.heapify(maxCourses)
        daysTaken = 0
        for courseDuration, courseDeadline in courses:
            heapq.heappush(maxCourses, -courseDuration)
            daysTaken += courseDuration
            if daysTaken > courseDeadline:
                daysTaken += heapq.heappop(maxCourses)
        return len(maxCourses)
