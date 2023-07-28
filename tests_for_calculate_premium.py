from salary_project.calculate_premium import calculate_premium


class TestCalculatePremium:

    def test_01_with_not_sick_days_and_working_months_36(self):
        # setup  month_salary=25000, working_months=36, sick_days=False

        # action
        x = calculate_premium(month_salary=25000, working_months=36, sick_days=False)

        # assertions
        assert x == 99000

    def test_02_with_sick_days_and_working_months_36(self):
        # setup  month_salary=25000, working_months=36, sick_days=True

        # action
        x = calculate_premium(month_salary=25000, working_months=36, sick_days=True)

        # assertions
        assert x == 90000

    def test_03_with_not_sick_days_and_working_months_from_18_till_36(self):
        # setup  month_salary=25000, working_months=18, sick_days=True

        # action
        x = calculate_premium(month_salary=25000, working_months=18, sick_days=True)

        # assertions
        assert x == 75000

    def test_04_with_not_sick_days_and_working_months_from_18_till_36(self):
        # setup  month_salary=25000, working_months=18, sick_days=False

        # action
        x = calculate_premium(month_salary=25000, working_months=18, sick_days=False)

        # assertions
        assert x == 84000

    def test_05_with_not_sick_days_and_working_months_from_3_till_18(self):
        # setup  month_salary=25000, working_months=3, sick_days=False

        # action
        x = calculate_premium(month_salary=25000, working_months=3, sick_days=False)

        # assertions
        assert x == 54000

    def test_06_with_not_sick_days_and_working_months_from_3_till_18(self):
        # setup  month_salary=25000, working_months=3, sick_days=True

        # action
        x = calculate_premium(month_salary=25000, working_months=3, sick_days=True)

        # assertions
        assert x == 45000

    def test_07_with_sick_days_and_working_months_from_3_till_18(self):
        # setup  month_salary=25000, working_months=3, sick_days=True

        # action
        x = calculate_premium(month_salary=25000, working_months=3, sick_days=True)

        # assertions
        assert x == 45000

    def test_08_less_then_3_working_months(self):
        # setup  month_salary=25000, working_months=3, sick_days=False

        # action
        x = calculate_premium(month_salary=25000, working_months=1, sick_days=False)

        # assertions
        assert x is None











