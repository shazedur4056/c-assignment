# ======
# Student Name : Rahman Md Shazedur
# Student ID   : M25W7502
# Course       : Fundamentals of Algorithms
# Program      : Midpoint Rule
# =====


class StudentInformation:

    full_name = "Rahman Md Shazedur"

    student_id = "M25W7502"


class MidpointIntegration:


    def mathematical_function(
        self,
        x
    ):

        return x * x


    def calculate_integral(

        self,

        lower_limit,

        upper_limit,

        total_intervals

    ):


        step_size = (
            upper_limit
            -
            lower_limit
        ) / total_intervals


        approximated_integral = 0


        for interval_position in range(
            total_intervals
        ):


            midpoint_position = (

                lower_limit

                +

                (
                    interval_position
                    +
                    0.5
                )

                *

                step_size

            )


            approximated_integral += (

                self
                .mathematical_function(
                    midpoint_position
                )

            )


        approximated_integral *= (
            step_size
        )


        return (
            approximated_integral
        )



midpoint_solver = (
    MidpointIntegration()
)


final_result = (

    midpoint_solver

    .calculate_integral(

        0,
        2,
        10

    )

)


print(
    StudentInformation.full_name
)

print(
    StudentInformation.student_id
)

print(
    "Midpoint Result =",
    final_result
)