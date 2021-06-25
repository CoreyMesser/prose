from services import Cards, Reader


class ApiControllers(Cards, Reader):

    def generate_prompt(self, params):
        self.concept_loop(params)

    def generate_file(self, params):
        self.generate_prompt_file(params=params)

    def get_prompt(self, params):
        return self._get_single_prompt(p_id=params)

    def get_random_selection(self, params):
        return self._get_prompt(how_many=params['how_many'])

    def get_prompt_set(self, params):
        return self.generate_prompt_file_set(params=params)
