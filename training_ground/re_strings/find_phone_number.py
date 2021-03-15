import re


def find_phone_number(text: str) -> list:
    return re.findall(r'\+38 0\d{2} \d{3} \d{4}', text)


if __name__ == "__main__":
    t = """
 London (CNN)Spain, Germany, France and Italy have become the latest European countries to temporarily halt the rollout of the Oxford-AstraZeneca Covid-19 vaccine over a small number of blood clot concerns, going against the advice of international medical agencies as a third wave of infections looms over the continent.

Spain will stop using the vaccine for two weeks, the country's Health Minister Carolina Darias announced in a nationally televised news conference Monday.
It's a "temporary and precautionary" suspension, she said, "until the risks can be evaluated by the European Medicines Agency."
After initially standing by the safety of the vaccine, German health minister Jens Spahn said Monday that the country would pause inoculations as a precaution, following reports of a handful of cases of blood clots in people vaccinated with the AstraZeneca shot in Denmark and Norway.
France and Italy also halted their rollouts of the vaccine Monday, pending review by the EU's medicines regulator, the European Medicines Agency (EMA), although the body later reiterated its advice that countries stick to the rollout.
"We have decided to suspend the use of AstraZeneca as a precautionary measure and are hoping to resume it quickly if the EMA's advice allows it," French President Emmanuel Macron said at Monday news conference.
The suspensions came hours after prosecutors in northern Italy ordered a batch of the vaccine to be seized, citing a man who fell ill and died after taking a shot. Italy's medicines agency also suspended the use of the AstraZeneca vaccine "as a precaution and temporarily," prior to the EMA meeting, the Italian medicines agency AIFA announced Monday.
Ireland halts use of AstraZeneca vaccine following blood clot reports in Norway +38 063 611 5852
Ireland halts use of AstraZeneca vaccine following blood clot reports in Norway
Much of Europe has now halted the shot for the time being, following the fatality of one woman in Denmark that has yet to be linked to a vaccine. Another death was also reported in Norway on Monday, along with a handful of non-fatal cases in both countries.
The suspensions go against the advice of the World Health Organization, the EMA and the pharmaceutical giant itself, all of whom have said there is no evidence of a link with clotting and that rollouts should continue while the reports are investigated.
"As of today, there is no evidence that the incidents are caused by the vaccine and it is important that vaccination campaigns continue so that we can save lives and stem severe disease from the virus," the WHO said in a statement to CNN. The organization added it was assessing the latest reports, but said any change in its recommendations would be "unlikely."
The EMA also reiterated that countries should continue their rollouts, adding that it would meet on Thursday to discuss the concerns but that the benefit of vaccinations outweigh any potential risks.
"While its investigation is ongoing, EMA currently remains +38 058 654 1257 of the view that the benefits of the AstraZeneca vaccine in preventing COVID-19, with its associated risk of hospitalisation and death, outweigh the risks of side effects," the agency said.
More than 11 million AstraZeneca jabs have been delivered in the UK, which is now one of few major European countries still backing the vaccine. Spahn said he spoke with his counterpart in the UK before halting Germany's rollout.
AstraZeneca doubled down on the safety of its shots Sunday, saying that a careful review of the 17 million people inoculated with it in the EU and Britain found again that there was "no evidence" of a link with clots.
It found that of those millions of people, there have been 15 events of deep vein thrombosis (DVT) and 22 events of pulmonary embolism reported after vaccination; lower than the number that would be expected to occur naturally within that population size.
Nonetheless, the death of one woman in Denmark prompted a number of countries to pause their rollouts until reviews have been conducted. The Danish Medicines Agency said on Monday the woman in question had an "unusual" combination of symptoms before she died.
AstraZeneca says &#39;no evidence&#39; of blood clot risk from vaccine as countries suspend its use
AstraZeneca says 'no evidence' of blood clot risk from vaccine as countries suspend its use
Later on Monday, Norway's Rikshospitalet hospital reported the death of another inoculated person with severe cases of blood clots, bleeding and low platelet count.
In the Netherlands, a lab that monitors the use of pharmaceuticals said it has received reports of 10 instances of blood clots in people who received the AstraZeneca Covid-19 vaccine, but none had the low blood platelet condition reportedly observed in Norway and Denmark.
Over the weekend Ireland and the Netherlands joined the pack of countries pausing their use of the AstraZeneca vaccine. The chairwoman of Ireland's vaccination advisory committee said it took the step to "maintain confidence" in the country's inoculation program. The Dutch government said its move was "precautionary" and would last for two weeks; this came just days after health minister Hugo de Jonge said there was "no cause for concern" over the shot.
The UK has by far led the way in administering the AstraZeneca vaccine, with more than 11 million people receiving a dose, and it too has stood by the shot. Real-world data from the country has also shown it is having a significant impact in reducing Covid-19 hospitalizations.
A single dose of the vaccine reduces the risk of hospitalization from Covid-19 by more than 80% in people aged over 80, data from Public Health England showed earlier this month. The vaccine is given in two doses, though countries differ in how far apart they are spreading those shots.
    """
    print(find_phone_number(t))
