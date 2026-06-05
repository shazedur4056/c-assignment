# ===
# Student Name : Rahman Md Shazedur
# Student ID   : M25W7502
# Program      : Simpson Rule
# ===


class StudentInformation:

    full_name = "Rahman Md Shazedur"

    student_id = "M25W7502"


class SimpsonIntegration:


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


        approximated_integral = (

            self
            .mathematical_function(
                lower_limit
            )

            +

            self
            .mathematical_function(
                upper_limit
            )

        )


        for interval_position in range(
            1,
            total_intervals
        ):


            x_value = (
                lower_limit
                +
                interval_position
                *
                step_size
            )


            if (
                interval_position
                %
                2
                ==
                0
            ):

                approximated_integral += (

                    2
                    *
                    self
                    .mathematical_function(
                        x_value
                    )

                )

            else:

                approximated_integral += (

                    4
                    *
                    self
                    .mathematical_function(
                        x_value
                    )

                )


        approximated_integral *= (
            step_size
            /
            3
        )


        return (
            approximated_integral
        )



solver = (
    SimpsonIntegration()
)


result = (
    solver
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
    "Simpson Result =",
    result
)