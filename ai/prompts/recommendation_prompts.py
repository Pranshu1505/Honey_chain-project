"""Recommendation Prompts - Template prompts for AI recommendations"""


class RecommendationPrompts:
    """Collection of recommendation prompt templates"""
    
    # Health recommendation prompts
    HEALTH_EXCELLENT = """
    ✅ Hive Health: EXCELLENT
    
    Your hive is in excellent condition with a health score of {score:.0f}/100.
    
    • Temperature stability is optimal ({temp_avg:.1f}°C)
    • Humidity levels are well-maintained ({humidity_avg:.1f}%)
    • Weight gain trend is positive ({weight_trend:.3f} kg/day)
    • Hive activity is normal ({activity_level})
    
    Continue with current management practices and monitor regularly.
    """
    
    HEALTH_GOOD = """
    🟢 Hive Health: GOOD
    
    Your hive is healthy with a health score of {score:.0f}/100.
    
    Focus areas to monitor:
    • {param_1}
    • {param_2}
    
    Recommendations:
    1. Continue regular monitoring (3-5 days)
    2. Check internal conditions if any parameter worsens
    3. Maintain current feeding/supplementation schedule
    """
    
    HEALTH_FAIR = """
    🟡 Hive Health: FAIR
    
    Your hive needs attention with a health score of {score:.0f}/100.
    
    Primary concerns:
    • {concern_1}
    • {concern_2}
    
    Immediate actions:
    1. Perform detailed physical inspection within 48 hours
    2. {action_1}
    3. {action_2}
    4. Recheck condition in 3 days
    """
    
    HEALTH_POOR = """
    🔴 URGENT - Hive Health: POOR
    
    Your hive requires immediate intervention. Health score: {score:.0f}/100
    
    Critical issues:
    • {critical_1}
    • {critical_2}
    • {critical_3}
    
    TAKE IMMEDIATE ACTION:
    1. Inspect hive TODAY
    2. {urgent_action_1}
    3. {urgent_action_2}
    4. Contact a local beekeeping expert if issues persist
    
    Monitor continuously over next 48 hours.
    """
    
    # Disease recommendation prompts
    DISEASE_DETECTED = """
    ⚠️ Disease Risk Alert: {disease_name}
    
    Risk Level: {risk_level} (Probability: {probability:.1f}%)
    
    What this means:
    {disease_description}
    
    Recommended actions:
    {recommendations}
    
    Monitoring checklist:
    □ Look for symptoms during next inspection
    □ Track affected bee population
    □ Monitor colony strength
    □ Recheck condition in 7 days
    """
    
    VARROA_MITE_ALERT = """
    🦟 Varroa Mite - MONITOR CLOSELY
    
    Risk Level: {risk_level} (Probability: {probability:.1f}%)
    
    Why this matters:
    Varroa mites are the #1 threat to honeybee colonies.
    
    Action Plan:
    1. Inspect bees and brood for visible mites
    2. Use a sugar shake test (100 bees shaken in powdered sugar)
    3. Monitor for increased bee mortality
    4. If infestation confirmed:
       - Consider treatment options (formic acid, thymol, or acaricides)
       - Recheck population in 2-3 weeks
    5. Continue monitoring and retest in 30 days
    """
    
    NOSEMA_ALERT = """
    🦠 Nosema Disease - Increased Risk
    
    Risk Level: {risk_level} (Probability: {probability:.1f}%)
    
    Prevention & Response:
    1. Monitor bee dysentery (fecal spotting on hive entrance)
    2. Ensure hive has adequate ventilation
    3. Reduce hive humidity (check humidity: {humidity:.1f}%)
    4. Provide fresh honey and pollen sources
    5. If symptoms found:
       - Perform hive sanitation
       - Consider medication options
       - Monitor for next 2-3 weeks
    """
    
    FOULBROOD_ALERT = """
    🏥 European Foulbrood - SERIOUS CONCERN
    
    Risk Level: {risk_level} (Probability: {probability:.1f}%)
    
    This is a reportable disease - notify local authorities if confirmed.
    
    Inspection Checklist:
    □ Check for diseased larvae (brown, twisted, ropy texture)
    □ Look for irregular brood patterns
    □ Smell for characteristic foul odor
    □ Check temperature stability ({temp_avg:.1f}°C)
    □ Assess hive humidity levels
    
    If confirmed:
    1. Notify local apiary inspector immediately
    2. Do not move equipment between hives
    3. Follow professional treatment guidance
    4. Quarantine affected hive
    """
    
    # Harvest recommendation prompts
    HARVEST_READY = """
    🍯 HARVEST READY
    
    Your hive is at optimal harvest weight!
    
    Current Status:
    • Current weight: {current_weight:.1f} kg
    • Target weight: {target_weight:.1f} kg
    • Status: READY FOR HARVEST
    
    Harvest Instructions:
    1. Choose a warm, sunny day
    2. Smoke gently to encourage bees downward
    3. Remove honey super (take only surplus)
    4. Leave enough for hive's winter stores
    5. Extract within 24-48 hours
    
    Post-Harvest:
    • Feed bees if needed for winter preparation
    • Provide clean water source
    • Monitor for late-season disease issues
    """
    
    HARVEST_APPROACHING = """
    🍯 Harvest Window Approaching
    
    Estimated harvest time: {days_to_harvest} days
    
    Current Status:
    • Current weight: {current_weight:.1f} kg
    • Target weight: {target_weight:.1f} kg
    • Growth rate: {growth_rate:.3f} kg/day
    • Season progress: {season_progress:.0f}%
    
    Preparation Checklist:
    □ Gather/prepare honey extraction equipment
    □ Schedule harvesting date
    □ Ensure bees have adequate winter food store
    □ Monitor weather for harvesting conditions
    □ Plan for post-harvest feeding if needed
    
    Check again in 3-5 days for updates.
    """
    
    HARVEST_DELAYED = """
    📉 Harvest Delayed
    
    Your hive needs more time before harvest.
    
    Current Status:
    • Current weight: {current_weight:.1f} kg
    • Target weight: {target_weight:.1f} kg
    • Estimated harvest: {days_to_harvest}+ days
    
    Reasons for delay:
    • {reason_1}
    • {reason_2}
    
    Support Actions:
    1. Monitor nectar flow conditions
    2. Ensure pollen and water sources available
    3. Check for disease or pest issues
    4. Maintain hive temperature
    5. Recheck weight in 1-2 weeks
    """
    
    # Seasonal recommendation prompts
    SPRING_GUIDE = """
    🌸 SPRING MANAGEMENT GUIDE
    
    Focus: Colony Buildup
    
    Essential Tasks:
    1. Provide protein supplement (pollen patties)
    2. Monitor brood patterns closely
    3. Prepare honey supers for flow
    4. Watch for swarming behavior
    5. Treat for varroa mites as needed
    6. Ensure adequate honey stores
    
    Monitoring Schedule:
    • Inspect every 7-10 days
    • Check for: disease, pests, swarming signs
    • Monitor population growth
    
    Expected Outcomes:
    • Colonies should increase 5-8 frames of bees
    • Brood patterns should be solid
    • Honey production ramping up by late spring
    """
    
    SUMMER_GUIDE = """
    ☀️ SUMMER MANAGEMENT GUIDE
    
    Focus: Honey Production
    
    Essential Tasks:
    1. Add honey supers as needed
    2. Maintain adequate ventilation
    3. Provide water source (heat stress)
    4. Minimize hive disturbances
    5. Monitor for swarming (prevent emergency cells)
    6. Continue disease/pest monitoring
    
    Monitoring Schedule:
    • Inspect every 10-14 days (during flow)
    • Focus on: honey stores, pest levels
    • Check for congestion or problems
    
    Expected Outcomes:
    • Maximum honey production
    • Strong bee population
    • Supers filling with honey
    """
    
    FALL_GUIDE = """
    🍂 FALL MANAGEMENT GUIDE
    
    Focus: Harvest & Winter Prep
    
    Essential Tasks:
    1. Harvest honey at peak
    2. Treat for varroa mites (critical timing)
    3. Ensure winter food stores (60+ lbs)
    4. Consolidate weak colonies
    5. Replace failing queens
    6. Prepare for winter
    
    Monitoring Schedule:
    • Inspect every 7-10 days through treatment
    • Track: food stores, pest levels, hive strength
    • Assess winter readiness
    
    Expected Outcomes:
    • Successful honey harvest
    • Reduced varroa population
    • Colonies prepared for dormancy
    """
    
    WINTER_GUIDE = """
    ❄️ WINTER MANAGEMENT GUIDE
    
    Focus: Colony Survival
    
    Essential Tasks:
    1. Minimize hive disturbances
    2. Monitor food consumption
    3. Ensure proper ventilation (NO moisture buildup)
    4. Protect from extreme cold
    5. Watch for mice/predators
    6. Plan for spring
    
    Monitoring Schedule:
    • Check hive weight (hefty test)
    • Inspect minimally (warm days only)
    • Monitor food consumption
    
    Expected Outcomes:
    • Colonies in tight clusters
    • Steady food consumption
    • Preparation for spring expansion
    """
    
    @staticmethod
    def format_recommendation(template: str, **kwargs) -> str:
        """Format a recommendation template with provided data"""
        try:
            return template.format(**kwargs)
        except KeyError as e:
            return f"Template error: Missing key {e}"
