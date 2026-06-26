#!/usr/bin/env python3
import os, csv
ROOT="WOW Book – This Is How You Walk on Water"
SUBS=["00 Needs Review – Possible Book Content","01 Manuscript – Chapters",
      "06 Visuals for Book","10 Marketing – Posts, Videos, Captions"]

# n,title,base,person,scene,emotion,hook,seed, scr_ref,scr_text,theme,note
C=[
(1,"In the Beginning: James and Margaret","In_the_Beginning_James_and_Margaret",True,
 "an old family photograph dissolving into golden light; a baby cradled by unseen hands; roots beneath a calm sea","origins and divine foreknowledge",
 "Before I had a name, God already knew my story.","My story didn't begin with me - it began in the heart of God.",
 "Psalm 139:16","Thine eyes did see my substance... and in thy book all my members were written.",
 "Origins & Foreknowledge","Where the story begins - James & Margaret, God's hand before birth. (Expand with personal details.)"),
(2,"Every Girl Needs a James","Every_Girl_Needs_a_James",True,
 "a strong oak beside still water; a young woman safe beneath a covering of warm light","covering, protection, and love",
 "Every girl needs a covering - mine pointed me to Christ.","God gave me a covering that taught me what holy love looks like.",
 "Psalm 68:6","God setteth the solitary in families.",
 "Covering & Family","The importance of godly covering and love. (Expand with personal details.)"),
(3,"The Foster Room Wasn't Home, But God Was","Foster_Room_Wasnt_Home_But_God_Was",True,
 "a small dim foster bedroom with a single window pouring warm divine light onto a child","belonging and God's presence in displacement",
 "The room wasn't home - but God was.","Even when I had no home, God was my dwelling place.",
 "Psalm 27:10","When my father and my mother forsake me, then the LORD will take me up.",
 "Belonging","The foster room season - displacement, yet God's nearness. (Expand with personal details.)"),
(4,"Scraps From the Table No More","Scraps_From_the_Table_No_More",True,
 "an empty plate transforming into an overflowing banquet table bathed in gold; a daughter seated as an honored guest","dignity and restoration",
 "I was raised on scraps - but God set a table for me.","God moved me from the floor to the table as a daughter, not a beggar.",
 "Psalm 23:5","Thou preparest a table before me in the presence of mine enemies.",
 "Dignity & Restoration","From crumbs to a prepared table - dignity restored. (Expand with personal details.)"),
(5,"The Footprint of Jesus in My Heart","Footprint_of_Jesus_in_My_Heart",False,
 "glowing footprints of light walking across water toward a radiant, gentle heart","intimacy and calling",
 "Jesus left His footprint on my heart.","I learned to walk in the very footprints Jesus left for me.",
 "1 Peter 2:21","...that ye should follow his steps.",
 "Intimacy & Calling","Calling, intimacy, healing, obedience - the footprint of Jesus. (Expand.)"),
(6,"When Everyone Walked Out, God Walked In","When_Everyone_Walked_Out_God_Walked_In",True,
 "an open doorway; silhouettes leaving into shadow while brilliant divine light enters","rejection turned to His presence",
 "When everyone walked out, God walked in.","The exit of people became the entrance of God.",
 "2 Timothy 4:17","Notwithstanding the Lord stood with me, and strengthened me.",
 "Rejection to Presence","Rejection, rebuilding, God's restoration. (Expand with personal details.)"),
(7,"Season of Shadows: When I Lost Everything, But God Kept Me","Season_of_Shadows_But_God",True,
 "a woman in a long valley of shadows held by a single shaft of golden light","loss and sustaining grace",
 "I lost so much - but God kept me.","In the season I lost everything, God kept the one thing the enemy wanted most: me.",
 "Psalm 23:4","Yea, though I walk through the valley of the shadow of death... thou art with me.",
 "Loss & Sustaining Grace","Losing much, finding God's presence. (Expand with personal details.)"),
(8,"The Fourth Dog: Grief at the Teeth of Another","The_Fourth_Dog_Grief_at_the_Teeth_of_Another",False,
 "a tender, sorrowful moment of comfort by soft candlelight; gentle hands and quiet peace","grief met by comfort",
 "Grief came again - and so did God's comfort.","Even in repeated grief, the God of all comfort drew near to me.",
 "Psalm 34:18","The LORD is nigh unto them that are of a broken heart.",
 "Grief & Comfort","Loss and grief, comforted by God. (Expand with personal details.)"),
(9,"The Daughter I Raised, the Silence I Carry","The_Daughter_I_Raised_the_Silence_I_Carry",True,
 "a mother's hands holding an empty photo frame in a quiet room touched by a fragile light of hope","silent grief and enduring love",
 "The silence I carry, God hears.","God hears the prayers I pray in silence over the ones I love.",
 "Psalm 56:8","...put thou my tears into thy bottle: are they not in thy book?",
 "Hidden Grief & Love","Carrying silent grief over a loved one, held by God. (Expand.)"),
(10,"I Stayed. They Strayed. But God Stayed With Me","I_Stayed_They_Strayed_But_God_Stayed",True,
 "a steadfast figure standing on a rock as waters part around her","faithfulness and companionship",
 "They strayed - but God stayed.","When others wandered, I stayed - and God stayed with me.",
 "Hebrews 13:5","I will never leave thee, nor forsake thee.",
 "Faithfulness","Faithful when others strayed; God never left. (Expand.)"),
(11,"The Hospital Stay: God Was in the Room","Hospital_Stay_God_Was_in_the_Room",True,
 "a hospital room transfigured by warm divine presence; light at the bedside; angelic peace","God's presence in sickness",
 "In the hospital room, God was there.","On the days the machines beeped and the nights felt long, God never left the room.",
 "Psalm 41:3","The LORD will strengthen him upon the bed of languishing.",
 "Presence in Sickness","The hospital stay - God present through illness. (Expand.)"),
(12,"Still Living With Rods: 39 Bolts, 39 Stripes","Still_Living_With_Rods_39_Bolts_39_Stripes",True,
 "a luminous silhouette with rods of golden light along the spine, 39 points of light, echoing Isaiah 53","pain redeemed into healing",
 "39 bolts in my back - by His 39 stripes I am healed.","I still live with rods, but by His stripes I am healed.",
 "Isaiah 53:5","...and with his stripes we are healed.",
 "Pain & Healing","Living with rods - 39 bolts, 39 stripes; redemptive healing. (Expand.)"),
(13,"The Four Nodules Diagnosis: Whose Report Will You Believe?","Four_Nodules_Whose_Report_Will_You_Believe",True,
 "a medical report dissolving into light as a woman chooses faith; scripture overpowering a diagnosis","faith over the report",
 "Whose report will you believe? I believe the report of the Lord.","The doctors gave a report - but I chose to believe the report of the Lord.",
 "Isaiah 53:1","Who hath believed our report? and to whom is the arm of the LORD revealed?",
 "Faith over the Report","Four nodules diagnosis; choosing God's report. (Expand.)"),
(14,"The Water Did Not Drown Me","The_Water_Did_Not_Drown_Me",True,
 "a woman rising up out of deep waters into light, not drowning but ascending","survival and deliverance",
 "The water did not drown me.","The waters that should have buried me became the place I learned to rise.",
 "Isaiah 43:2","When thou passest through the waters, I will be with thee.",
 "Survival & Deliverance","Passing through deep waters and not drowning. (Expand.)"),
(15,"The Dove Experiences: God Came Like a Dove","Dove_Experiences_God_Came_Like_a_Dove",False,
 "a radiant white dove descending in golden light over still water","peace and the Spirit's visitation",
 "God came to me like a dove.","When I needed peace, God came to me gentle as a dove.",
 "Matthew 3:16","...the Spirit of God descending like a dove, and lighting upon him.",
 "Peace & the Spirit","The dove experiences - the Spirit's gentle visitation. (Expand.)"),
(16,"The Giraffe Revelation: Seeing Higher","Giraffe_Revelation_Seeing_Higher",False,
 "a giraffe silhouette against dawn, eyes lifted high above the plain","elevated perspective and revelation",
 "God taught me to see higher.","God lifted my eyes to see what fear had hidden below.",
 "Colossians 3:2","Set your affection on things above, not on things on the earth.",
 "Vision & Perspective","The giraffe revelation - seeing higher. (Expand.)"),
(17,"Small Animals in the Kitchen: God Speaks in Strange Places","Small_Animals_in_the_Kitchen",False,
 "an ordinary kitchen touched with subtle wonder and warm light; the sacred in the mundane","God in the ordinary",
 "God speaks even in strange and ordinary places.","God taught me to listen, because He speaks even in the kitchen.",
 "1 Kings 19:12","...and after the fire a still small voice.",
 "God in the Ordinary","God speaking in unexpected, ordinary places. (Expand.)"),
(18,"Daniel 10: The Battle for Delayed Blessings","Daniel_10_Battle_for_Delayed_Blessings",False,
 "an angel breaking through dark storm clouds with an answer of light after a long battle","perseverance and unseen warfare",
 "Your blessing was delayed, not denied.","For twenty-one days heaven fought for me - the answer was on its way the whole time.",
 "Daniel 10:12","...from the first day... thy words were heard, and I am come for thy words.",
 "Spiritual Warfare / Delay","Daniel 10 - the battle behind delayed blessings. (Expand.)"),
(19,"It's Just a Shadow","Its_Just_a_Shadow",True,
 "a looming shadow revealed to be small against a great light; fear shrinking before faith","fearlessness",
 "It looked like a giant - it was just a shadow.","What loomed like a giant was only a shadow in the light of God.",
 "Psalm 27:1","The LORD is my light and my salvation; whom shall I fear?",
 "Fearlessness","Fear exposed as just a shadow. (Expand.)"),
(20,"This Time the Enemy Will Not Steal","This_Time_the_Enemy_Will_Not_Steal",True,
 "hands reclaiming stolen treasure wrapped in light; a gate closing on the thief","recovery and authority",
 "This time, the enemy will not steal.","I took back, in Jesus' name, everything the enemy tried to steal.",
 "Joel 2:25","And I will restore to you the years that the locust hath eaten.",
 "Recovery & Authority","Reclaiming what the enemy tried to steal. (Expand.)"),
(21,"The Tomb Has Been Rolled Away: I Will Rise","Tomb_Has_Been_Rolled_Away_I_Will_Rise",True,
 "an empty tomb with the stone rolled aside and brilliant resurrection light bursting out","resurrection and rising",
 "The stone is rolled away - I will rise.","What I buried in grief, God called out of the grave.",
 "Matthew 28:2","...the angel... came and rolled back the stone from the door.",
 "Resurrection","Resurrected dreams; the stone rolled away. (Expand.)"),
(22,"Dry Bones Rattling: It Is Finished","Dry_Bones_Rattling_It_Is_Finished",False,
 "a valley of dry bones coming alive with the breath of golden light","revival and the finished work",
 "Dry bones are rattling - it is finished.","God breathed, and what was dead in me began to live again.",
 "Ezekiel 37:5","Behold, I will cause breath to enter into you, and ye shall live.",
 "Revival / Finished Work","Dry bones living again; it is finished. (Expand.)"),
(23,"Fresh Fresh Fire: Burn for You","Fresh_Fresh_Fire_Burn_for_You",False,
 "a bright holy flame rekindled with golden sparks rising","renewal and passion",
 "Lord, send fresh fire - I'll burn for You.","I asked God for fresh fire, and my first love came alive again.",
 "2 Timothy 1:6","...stir up the gift of God, which is in thee.",
 "Renewal & Fire","Fresh fire; recommitment and passion. (Expand.)"),
(24,"I'm Coming Out at Midnight","Im_Coming_Out_at_Midnight",True,
 "prison doors flung open at midnight as golden light breaks the darkness","breakthrough at the darkest hour",
 "At midnight, I'm coming out.","I learned to praise at midnight - and the chains began to fall.",
 "Acts 16:26","...and at midnight... immediately all the doors were opened.",
 "Midnight Breakthrough","Praise and breakthrough at the darkest hour. (Expand.)"),
(25,"The Scroll Was in My Belly","The_Scroll_Was_in_My_Belly",True,
 "a glowing scroll of light held within; a prophet receiving the word inside","prophetic calling and the word within",
 "The scroll was in my belly - God's word became part of me.","God placed His word inside me until it became my very breath.",
 "Ezekiel 3:3","...eat this roll... and fill thy bowels with it.",
 "Prophetic Word Within","The scroll within - the word made part of her. (Expand.)"),
(26,"The Scroll of Survival: Living Testimony","Scroll_of_Survival_Living_Testimony",True,
 "an unrolling scroll inscribed with light; a living testimony written across water","survival and testimony",
 "My survival is a scroll - a living testimony.","My survival itself became a scroll the world could read.",
 "Revelation 12:11","And they overcame him by the blood of the Lamb, and by the word of their testimony.",
 "Testimony & Survival","Survival as a living testimony scroll. (Expand.)"),
(27,"Rise Above the Soil: Fruitful Emergence","Rise_Above_the_Soil_Fruitful_Emergence",False,
 "a seed breaking through dark soil into golden light, blossoming toward harvest","emergence and fruitfulness",
 "What was buried is rising - fruitful at last.","What looked buried was only planted, and now it is bearing fruit.",
 "John 12:24","Except a corn of wheat fall into the ground and die... it bringeth forth much fruit.",
 "Emergence & Fruitfulness","Buried like a seed, rising fruitful. (Expand.)"),
(28,"Faith Under Fire: I Still Believe","Faith_Under_Fire_I_Still_Believe",True,
 "a figure standing unharmed within flames, faith unshaken, a fourth presence in the fire","tested, unshaken faith",
 "Under fire, I still believe.","The fire did not consume me - it could not take my faith.",
 "Daniel 3:17","Our God whom we serve is able to deliver us from the burning fiery furnace.",
 "Tested Faith","Faith refined under fire; still believing. (Expand.)"),
(29,"I'm Dancing on the Grave I Once Lived In","Dancing_on_the_Grave_I_Once_Lived_In",True,
 "a woman joyfully dancing in light upon an empty grave, victory over death","triumphant joy",
 "I'm dancing on the grave I once lived in.","The place that was meant to bury me is the place I now dance.",
 "Psalm 30:11","Thou hast turned for me my mourning into dancing.",
 "Triumphant Joy","Dancing in victory over what once buried her. (Expand.)"),
(30,"This Is How You Walk on Water","This_Is_How_You_Walk_on_Water",True,
 "a radiant woman walking on shining water toward the light of Jesus at majestic dawn (signature image)","faith over fear, the culmination",
 "This is how you walk on water.","This is how you walk on water - eyes on Jesus, one step of faith at a time.",
 "Matthew 14:29","And he said, Come. And... Peter... walked on the water, to go to Jesus.",
 "Faith Over Fear (Culmination)","The culminating chapter - living beyond fear, walking on water. (Expand.)"),
]

def vp(n,title,person,scene,emotion):
    mn=" Feature Loretta 'Lolo' Hall's likeness (Higgsfield Soul 'Coral Elegance Unveiled') as the woman." if person else ""
    return (f"Cinematic, premium faith-based book illustration for 'This Is How You Walk on Water' - "
            f"Chapter {n}: {title}. Scene: {scene}. Mood: {emotion}. Style: Heavenly Hands Divine - water motif, "
            f"divine golden light, deep jewel tones (navy, teal, gold), tasteful, hopeful, fine-art testimony "
            f"illustration.{mn} Vertical 2:3, high resolution, no text, no watermark.")
def sv(n,scene,hook):
    return (f"15-30s vertical reel (9:16). HOOK (0-3s): \"{hook}\" VISUALS: {scene}; slow cinematic push-in, "
            f"water and golden light, soft particles. TONE: Faith Over Fear - intimate, uplifting. Optional captions. "
            f"END CARD: 'This Is How You Walk on Water - Chapter {n}'.")
def lv(n,scene,emotion):
    return (f"60-90s testimony teaser (9:16). ARC: open in the weight of {emotion}; move through the moment ({scene}); "
            f"resolve into hope and light. Loretta 'Lolo' Hall voiceover over soft cinematic b-roll of water and golden "
            f"light; subtle scripture overlay; build to the turning point. CTA: 'Read Chapter {n} of This Is How You Walk on Water.'")
def vo(seed,hook,n):
    return (f"Warm, intimate, faith-filled - Loretta 'Lolo' Hall. Pace: slow, tender, hopeful. SEED LINE: \"{seed}\" "
            f"~120-150 words (long) / ~30 words (reel). End with a gentle invitation to keep walking in faith. "
            f"CAPTION: \"{hook}\" - from Chapter {n} of This Is How You Walk on Water. #FaithOverFear #WalkOnWater #HeavenlyHandsDivine")

os.makedirs(ROOT,exist_ok=True)
for s in SUBS: os.makedirs(os.path.join(ROOT,s),exist_ok=True)
master=[["Chapter","Chapter_Title","Scripture_Ref","Scripture_Text","Theme","Testimony_Notes",
         "Chapter_Draft","Book_Visual_Prompt","Short_Video_Prompt","Long_Video_Prompt",
         "Voiceover_Caption","Status","Asset_Base_Name","Target_Visual_File"]]
for (n,title,base,person,scene,emotion,hook,seed,sref,stext,theme,note) in C:
    ch=f"CH{n:02d}"; bn=f"WOWBOOK_{ch}_{base}_V1_Draft"
    V,S,L,VC=vp(n,title,person,scene,emotion),sv(n,scene,hook),lv(n,scene,emotion),vo(seed,hook,n)
    draft="(to be written - see 01 Manuscript folder)"
    man=os.path.join(ROOT,SUBS[1],ch); vis=os.path.join(ROOT,SUBS[2],ch); mkt=os.path.join(ROOT,SUBS[3],ch)
    for d in (man,vis,mkt): os.makedirs(d,exist_ok=True)
    open(os.path.join(man,f"WOWBOOK_{ch}_{base}_Manuscript_V1_Draft.md"),"w").write(
        f"# {ch} – {title}\n\n**Scripture:** {sref} — \"{stext}\"\n**Theme:** {theme}\n**Status:** Not Started\n\n"
        f"## Testimony Notes\n{note}\n\n## Chapter Draft\n_(Paste Loretta's full chapter testimony here.)_\n")
    open(os.path.join(vis,f"{bn}.md"),"w").write(
        f"# {ch} – {title}\n**Scripture:** {sref}\n**Theme:** {theme}\n**Target visual file:** `{bn}.png`\n**Status:** Not Started\n\n"
        f"## Book Visual Prompt\n{V}\n")
    open(os.path.join(mkt,f"WOWBOOK_{ch}_{base}_Media_V1_Draft.md"),"w").write(
        f"# {ch} – {title}\n**Scripture:** {sref}\n**Theme:** {theme}\n**Status:** Not Started\n\n"
        f"## Short Video Prompt (Reel)\n{S}\n\n## Long Video Prompt (Teaser)\n{L}\n\n## Voiceover / Caption\n{VC}\n")
    master.append([ch,title,sref,stext,theme,note,draft,V,S,L,VC,"Not Started",base,f"{bn}.png"])
with open(os.path.join(ROOT,"WOWBOOK_Production_Map.csv"),"w",newline="") as f:
    csv.writer(f).writerows(master)
open(os.path.join(ROOT,SUBS[0],"READ_ME_Needs_Review.md"),"w").write(
"""# 00 Needs Review – Possible Book Content

Holds material that MAY belong in the Walk On Water book but is NOT in the 30-chapter map. Nothing is deleted; review and decide.

## Candidates (review before moving)
- The 30 WOW devotional companion PDFs (prayer/scripture devotionals).
- EDU Education Center ebook content (overlapping testimony themes).
- Older prayers, declarations, scrolls, or notes not mapped to CH01–CH30.

## Lane separation
- WOWB = product scrolls / CSV / Manus / Stripe (store lane). NOT this folder.
- WOWBOOK = the book 'This Is How You Walk on Water' (this folder).
""")
print("WOWBOOK v2: enriched 30 chapters with Scripture, Theme, Testimony Notes, Chapter Draft + prompts + status.")
