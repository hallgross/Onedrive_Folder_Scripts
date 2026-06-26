#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
import textwrap, os, re

W,H=letter
NAVY=HexColor('#0b2a4a'); BLUE=HexColor('#1b6ca8'); GOLD=HexColor('#c9a227')
TEAL=HexColor('#1b4d5e'); INK=HexColor('#15202b'); SOFT=HexColor('#5b6b7b')

NUMWORD=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
"Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty",
"Twenty-One","Twenty-Two","Twenty-Three","Twenty-Four","Twenty-Five","Twenty-Six","Twenty-Seven",
"Twenty-Eight","Twenty-Nine","Thirty"]

# Each chapter: title, focus, ref, verse, story(list), prayer, declarations(list)
CH=[
{"t":"The Prayer of Jabez","f":"God enlarged my life beyond my pain.","ref":"1 Chronicles 4:10",
 "v":"And Jabez called on the God of Israel, saying, Oh that thou wouldest bless me indeed, and enlarge my coast... And God granted him that which he requested.",
 "s":["There was a time when I believed my life would always be defined by pain.",
 "Long before Heavenly Hands Divine, before the ministry, before the books, before people knew my name, there was simply a woman crying out to God. I had experienced loss, sickness, disappointment, rejection, and seasons that seemed too heavy to carry. There were moments when I wondered if my story would ever become anything more than survival.",
 "Yet in the middle of those difficult seasons, God began changing my prayer.",
 "Instead of asking Him only to remove the pain, He taught me to pray for something greater. Like Jabez, I began asking God to enlarge my territory - not for recognition, but so my life could become a testimony of His faithfulness.",
 "Looking back, I can see that God answered that prayer in ways I never imagined. He enlarged my faith before He enlarged my influence. He enlarged my compassion before He enlarged my ministry. He enlarged my vision before He enlarged my opportunities.",
 "The very places where I thought my life had ended became the places where God began something new. My scars became reminders of His healing. My tears became seeds of hope for someone else. My testimony became proof that God can take what was broken and use it for His glory.",
 "If you are reading this today, perhaps you are praying your own Prayer of Jabez. Maybe you feel overlooked, discouraged, or uncertain about what comes next. I want you to know that God sees far beyond your current circumstances. He specializes in enlarging lives that have been shaped by hardship.",
 "Don't let your past define your future. Let God's promise define it.",
 "The same God who heard my cry is listening to yours. He has not forgotten you. Your pain is not the end of your story - it may be the very beginning of the purpose He has been preparing all along."],
 "ins":["One day you'll look back, just as I have, and realize that God wasn't simply bringing you through the storm. He was enlarging your life beyond anything you could have imagined."],
 "p":"Father, like Jabez I ask You to bless me indeed and enlarge my territory. Take me beyond my pain into the purpose You ordained. Keep Your hand upon me and let no harm overtake me. Enlarge my faith, my influence, and my joy, that my life may glorify You. In Jesus' name, Amen.",
 "d":["I declare God is enlarging my life beyond my pain.","I declare His hand is upon me.","I declare my territory is increasing.","I declare blessing is overtaking me.","I declare my best days are ahead."]},

{"t":"James & Margaret","f":"Where my story began and God's hand before I was born.","ref":"Psalm 139:16",
 "v":"Thine eyes did see my substance, yet being unperfect; and in thy book all my members were written, which in continuance were fashioned, when as yet there was none of them.",
 "s":["Before I took my first breath, God already knew my name. My story did not begin with me - it began in the heart of God and through the lives of those He placed before me.",
 "When I consider where I come from, I see God's hand stitched through every generation, every hardship, every prayer prayed over a child who did not yet exist. Nothing about my beginning was an accident.",
 "If your beginning was hard, take heart. God writes purpose into roots the world overlooks. The same hand that fashioned me in secret has been writing your story since before you were born."],
 "p":"Father, thank You that You saw me before anyone else did. Thank You for the hands and prayers that carried my beginning. Redeem my roots, heal my family line, and let the story You started in me be finished for Your glory. In Jesus' name, Amen.",
 "d":["I declare I was known by God before I was born.","I declare my roots are redeemed.","I declare purpose was written into my beginning.","I declare my family line is blessed.","I declare God finishes what He starts."]},

{"t":"Every Girl Needs a James","f":"The importance of godly covering and love.","ref":"Ephesians 5:25",
 "v":"Husbands, love your wives, even as Christ also loved the church, and gave himself for it.",
 "s":["There is a covering God designs for every daughter - a love that protects, honors, and points her to Christ. I learned the value of godly covering by both its presence and its absence.",
 "Real love does not control; it covers. It does not diminish; it strengthens. When God places the right people around you, they become a shelter where your gifts can grow safe and unafraid.",
 "If you are still waiting for that covering, do not settle. Let God be your covering first. He loves like Christ loved the church - completely, sacrificially, and forever."],
 "p":"Father, thank You for being my covering and my defender. Surround me with love that honors You. Heal the places where covering was missing, and teach me to receive and to give godly love. In Jesus' name, Amen.",
 "d":["I declare God is my covering.","I declare I am honored and protected.","I declare I will not settle for less than God's best.","I declare godly love surrounds me.","I declare I am worthy of holy love."]},

{"t":"When Everyone Walked Away","f":"Learning that God never left me.","ref":"Psalm 27:10",
 "v":"When my father and my mother forsake me, then the LORD will take me up.",
 "s":["I have known the ache of empty chairs and silent phones - the sting of being left by people I believed would stay. Rejection has a way of whispering that something is wrong with you.",
 "But in the very season everyone walked away, I discovered the One who never does. God did not just stay near; He drew closer. What people meant as abandonment, He used as an invitation into His presence.",
 "If you feel forsaken today, hear this: the exit of people is never the end of your story. The God who remains is rebuilding your life with His own hands."],
 "p":"Father, where people have walked away, thank You for walking in. Heal the wound of rejection. Remind me that I am never alone, for You will never leave me nor forsake me. Rebuild what was broken. In Jesus' name, Amen.",
 "d":["I declare God never left me.","I declare I am not forsaken.","I declare my worth is not decided by who left.","I declare I am held by God.","I declare I am being rebuilt stronger."]},

{"t":"The Season of Shadows","f":"Losing so much, yet finding God's presence.","ref":"Psalm 23:4",
 "v":"Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.",
 "s":["There was a season when loss came in waves - and the shadows felt long. Grief has a weight that words cannot fully carry.",
 "Yet even in the valley, I was not alone. The Shepherd walked every dark step with me. I learned that a shadow only exists because a light is shining nearby. God's presence was that light.",
 "If you are walking through shadows now, do not be afraid. You are passing through - not staying. And the One beside you knows the way to the other side."],
 "p":"Father, in my season of shadows, thank You for being present. Comfort my grief, steady my steps, and lead me through the valley into Your light. I will fear no evil, for You are with me. In Jesus' name, Amen.",
 "d":["I declare I am passing through, not staying.","I declare God is with me in the valley.","I declare His presence is my light.","I declare I will fear no evil.","I declare joy is coming."]},

{"t":"God Kept Me Alive","f":"Surgeries, sickness, and His sustaining hand.","ref":"Psalm 118:17",
 "v":"I shall not die, but live, and declare the works of the LORD.",
 "s":["There were moments my body was weak and the road of sickness was long - surgeries, recoveries, and nights I wondered if I would see morning.",
 "But God kept me. His sustaining hand held me when medicine reached its limit. I am living proof that He is a keeper, a healer, and a giver of life.",
 "If you are fighting for your health today, hold on to this word: you shall not die, but live. Your story is not finished, and your testimony is still being written."],
 "p":"Father, thank You for keeping me alive. You are Jehovah Rapha, my healer. Sustain my body, renew my strength, and let my life declare Your works. I shall live and not die. In Jesus' name, Amen.",
 "d":["I declare I shall live and not die.","I declare God's sustaining hand is upon me.","I declare healing is my portion.","I declare my body is renewed.","I declare I will declare His works."]},

{"t":"Healing in Stages","f":"Learning to trust God even when healing came slowly.","ref":"Philippians 1:6",
 "v":"Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ.",
 "s":["Not every healing came at once. Some came in stages - a little more strength today, a little more peace tomorrow. The slowness tested my trust.",
 "I learned that God is not careless with our healing; He is thorough. What takes time is often what lasts. He was performing a good work in me, step by step.",
 "If your healing feels slow, do not lose heart. The One who began it will complete it. Slow is not stopped, and gradual is still God."],
 "p":"Father, thank You that You heal completely, even when it comes in stages. Give me patience to trust Your process. Finish the good work You started in me - spirit, soul, and body. In Jesus' name, Amen.",
 "d":["I declare God is healing me completely.","I declare slow is not stopped.","I declare He will finish what He began.","I declare I trust His process.","I declare wholeness is coming."]},

{"t":"The Keys God Gave Me","f":"Doors only He could open.","ref":"Revelation 3:8",
 "v":"I know thy works: behold, I have set before thee an open door, and no man can shut it.",
 "s":["Some doors in my life could only be opened by God - doors no connection, effort, or striving could unlock. He handed me keys I did not earn.",
 "I learned to stop forcing locks that were never mine and to wait for the doors He set before me. What God opens, no one can shut; what He shuts, no one can pry open.",
 "If you are standing before a closed door, trust the Keeper of keys. Your appointed door is coming, and it will open right on time."],
 "p":"Father, thank You for the keys only You can give. Open the doors You have ordained for me and close the ones that are not mine. Give me wisdom to walk through the right ones in faith. In Jesus' name, Amen.",
 "d":["I declare God holds the keys to my life.","I declare the right doors are opening.","I declare no one can shut what He opens.","I declare my access is increasing.","I declare I walk through in faith."]},

{"t":"Becoming the Bride","f":"Learning identity in Christ.","ref":"Isaiah 61:10",
 "v":"He hath clothed me with the garments of salvation, he hath covered me with the robe of righteousness, as a bride adorneth herself with her jewels.",
 "s":["For a long time I searched for identity in roles, in people, in approval. None of it ever fit quite right.",
 "Everything changed when I discovered who I am in Christ - clothed in salvation, covered in righteousness, adorned like a bride. My identity was never something to earn; it was something to receive.",
 "If you have been unsure of who you are, look to Him. You are chosen, beloved, and beautifully His. That is the truest thing about you."],
 "p":"Father, thank You for clothing me in salvation and righteousness. Settle my identity in You. Let me see myself the way You see me - chosen, beloved, and adorned. In Jesus' name, Amen.",
 "d":["I declare my identity is in Christ.","I declare I am chosen and beloved.","I declare I am clothed in righteousness.","I declare I am beautifully His.","I declare I no longer strive to be enough."]},

{"t":"The Promise Floats","f":"When hope refused to sink.","ref":"Hebrews 6:19",
 "v":"Which hope we have as an anchor of the soul, both sure and stedfast.",
 "s":["There were times the weight of life should have sunk me. But the promise of God floated - it refused to go under, no matter how high the waters rose.",
 "Hope anchored my soul when everything else was unsteady. I learned that God's promises are buoyant; they rise to the top of every flood because they are sealed by His faithfulness.",
 "Whatever is trying to pull you down today, hold to the promise. It floats. And so will you."],
 "p":"Father, thank You that Your promise floats and Your hope anchors my soul. When the waters rise, keep me steady. I will not sink, for my hope is sure and stedfast in You. In Jesus' name, Amen.",
 "d":["I declare the promise of God floats.","I declare hope anchors my soul.","I declare I will not sink.","I declare His Word holds me up.","I declare I rise above every flood."]},

{"t":"Fishers of Men","f":"Discovering my ministry calling.","ref":"Matthew 4:19",
 "v":"And he saith unto them, Follow me, and I will make you fishers of men.",
 "s":["I did not always know I was called. Ministry found me in the middle of my own healing, when God whispered that my pain had a purpose for others.",
 "Following Jesus rearranged my life. He took my ordinary and made it useful for His kingdom. Becoming a fisher of men was not about a title - it was about obedience.",
 "If God is stirring a calling in you, do not shrink back. Follow Him, and He will make you into what He has called you to be."],
 "p":"Father, thank You for calling me. Make me a fisher of men. Use my story, my hands, and my voice to draw others to You. Here I am - send me. In Jesus' name, Amen.",
 "d":["I declare I am called by God.","I declare my pain has purpose.","I declare I am a fisher of men.","I declare my obedience changes lives.","I declare I will follow Him fully."]},

{"t":"The Wilderness Wasn't Empty","f":"God provided in dry seasons.","ref":"Deuteronomy 2:7",
 "v":"For the LORD thy God hath blessed thee in all the works of thy hand... thou hast lacked nothing.",
 "s":["My wilderness seasons looked empty from the outside - dry, quiet, lonely. But they were not empty at all.",
 "God met me there with manna I did not expect. He provided in ways the comfortable seasons never could. The wilderness became the place I learned His faithfulness firsthand.",
 "If you are in a dry place, look again. God is there, and you will lack nothing under His care."],
 "p":"Father, thank You that my wilderness is not empty. You provide manna in the desert and water from the rock. Sustain me, and let me lack nothing as I trust You. In Jesus' name, Amen.",
 "d":["I declare my wilderness is not empty.","I declare God provides in dry seasons.","I declare I lack nothing.","I declare His faithfulness sustains me.","I declare provision is on the way."]},

{"t":"After I Suffered Awhile","f":"Looking back at God's restoration.","ref":"1 Peter 5:10",
 "v":"But the God of all grace... after that ye have suffered a while, make you perfect, stablish, strengthen, settle you.",
 "s":["Suffering was not the end of my story - it was a chapter God used to make me whole. Looking back, I can see what I could not see in the middle of it.",
 "After I suffered a while, God restored. He made perfect, established, strengthened, and settled me. The very thing that tried to break me became the foundation He built upon.",
 "If you are still in the 'awhile,' keep going. Restoration follows the faithful. Your after is coming."],
 "p":"Father, God of all grace, thank You for restoration after suffering. Make me perfect, establish me, strengthen me, and settle me. Turn my pain into a foundation for Your glory. In Jesus' name, Amen.",
 "d":["I declare restoration follows my suffering.","I declare God is making me whole.","I declare I am established and strengthened.","I declare my after is coming.","I declare grace carries me."]},

{"t":"Taking the First Step","f":"Walking by faith before seeing the outcome.","ref":"2 Corinthians 5:7",
 "v":"For we walk by faith, not by sight.",
 "s":["The hardest part was always the first step - moving before I could see the outcome, obeying before I understood the plan.",
 "But faith is spelled with feet. God rarely shows the whole staircase; He asks for one step in the dark. Every time I stepped, the ground appeared beneath me.",
 "Whatever God is asking of you, take the step. You do not need the whole picture - you need the next move of obedience."],
 "p":"Father, give me courage to take the first step. I will walk by faith and not by sight. Steady me as I move before I see, and meet me with Your provision at every step. In Jesus' name, Amen.",
 "d":["I declare I walk by faith, not by sight.","I declare I will take the first step.","I declare the ground will appear as I move.","I declare obedience unlocks my future.","I declare God meets me in the step."]},

{"t":"Peace in the Storm","f":"Finding Jesus in difficult seasons.","ref":"Mark 4:39",
 "v":"And he arose, and rebuked the wind, and said unto the sea, Peace, be still. And the wind ceased, and there was a great calm.",
 "s":["Storms came that I did not choose - sudden, loud, and frightening. In the worst of them, I learned where peace really lives.",
 "Peace was not the absence of the storm; it was the presence of Jesus in it. The same voice that calmed the sea spoke calm into my soul.",
 "If the winds are howling around you, look for Jesus. He is not asleep to your need, and at His word the storm must still."],
 "p":"Father, speak peace over my storm. Quiet the winds in my mind and the waves in my heart. Let the calm of Your presence rule over every difficult season. Peace, be still. In Jesus' name, Amen.",
 "d":["I declare peace in my storm.","I declare Jesus is in my boat.","I declare the winds obey His voice.","I declare a great calm rests on me.","I declare fear does not rule me."]},

{"t":"The Unexpected Blessing","f":"When obedience brought abundance.","ref":"Luke 5:6",
 "v":"And when they had this done, they inclosed a great multitude of fishes: and their net brake.",
 "s":["I obeyed God once when it made no sense - cast the net again after a long, empty night. What followed was abundance I never saw coming.",
 "Obedience is the doorway to unexpected blessing. God multiplies what we surrender, and He often blesses us right where we had given up.",
 "If God is asking you to try again, do it. Your breakthrough may be one act of obedience away."],
 "p":"Father, thank You for unexpected blessing born of obedience. Give me the faith to cast the net again. Multiply what I surrender and fill my empty places with Your abundance. In Jesus' name, Amen.",
 "d":["I declare obedience brings abundance.","I declare I will cast the net again.","I declare unexpected blessing finds me.","I declare God multiplies my surrender.","I declare my empty places are being filled."]},

{"t":"Keeping My Eyes on Jesus","f":"Choosing faith over fear.","ref":"Hebrews 12:2",
 "v":"Looking unto Jesus the author and finisher of our faith.",
 "s":["When I looked at the waves, I began to sink. When I looked at Jesus, I could stand on the very thing that should have swallowed me.",
 "Fear grows when our eyes drift to the storm. Faith grows when our eyes return to Him. I learned to keep looking at the One who authors and finishes my faith.",
 "Wherever your eyes go, your heart will follow. Choose faith over fear - keep your eyes on Jesus."],
 "p":"Father, fix my eyes on Jesus. When fear pulls my gaze to the waves, turn me back to You. Author and finish my faith, and keep me standing on Your Word. In Jesus' name, Amen.",
 "d":["I declare my eyes are on Jesus.","I declare faith over fear.","I declare I will not sink.","I declare He authors and finishes my faith.","I declare I stand on His Word."]},

{"t":"No Weapon Formed Against Me","f":"Standing through attacks.","ref":"Isaiah 54:17",
 "v":"No weapon that is formed against thee shall prosper; and every tongue that shall rise against thee in judgment thou shalt condemn.",
 "s":["The attacks were real - words, schemes, seasons that tried to take me out. I will not pretend the warfare did not hurt.",
 "But I learned the verdict was already written. Weapons formed, but they did not prosper. I was not fighting for victory; I was standing in it.",
 "Whatever is rising against you, it will not have the final word. This is your heritage: no weapon formed against you shall prosper."],
 "p":"Father, thank You that no weapon formed against me shall prosper. I stand covered by the blood of Jesus. Silence every accusing tongue and dismantle every scheme. I rest in the victory already won. In Jesus' name, Amen.",
 "d":["I declare no weapon formed against me shall prosper.","I declare every accusing tongue is silenced.","I declare I stand in victory.","I declare I am covered by the blood.","I declare the battle is the Lord's."]},

{"t":"My Tomb Rolled Away","f":"God resurrected dreams I thought were gone.","ref":"Matthew 28:2",
 "v":"And, behold, there was a great earthquake: for the angel of the Lord descended from heaven, and came and rolled back the stone from the door.",
 "s":["I had buried dreams I thought were dead - sealed them behind a stone and walked away grieving.",
 "But God is a tomb-roller. He moved the stone I could not budge and breathed life into what I had given up. Resurrection is His specialty.",
 "If something in your life feels buried, do not write the ending yet. The stone is being rolled away, and what looked dead is about to live."],
 "p":"Father, roll away the stone over my buried dreams. Breathe resurrection life into what I thought was gone. The same power that raised Jesus lives in me. Let my dead places live again. In Jesus' name, Amen.",
 "d":["I declare my tomb is rolled away.","I declare buried dreams are resurrected.","I declare resurrection power lives in me.","I declare what looked dead will live.","I declare my best is not behind me."]},

{"t":"Walking on Water","f":"Living beyond fear.","ref":"Matthew 14:29",
 "v":"And he said, Come. And when Peter was come down out of the ship, he walked on the water, to go to Jesus.",
 "s":["The waters that should have drowned me became the place I learned to walk. Fear said stay in the boat; faith said come.",
 "Walking on water is simply trusting the One who calls you out. I stepped onto the impossible and found His hand holding mine.",
 "Whatever is calling you to fear, Jesus is calling you to come. Living beyond fear begins with one faith-filled step onto the water."],
 "p":"Father, You are calling me out of the boat. Give me faith to walk on water and to keep my eyes on You. When I waver, catch me. I choose to live beyond fear. In Jesus' name, Amen.",
 "d":["I declare I walk on water by faith.","I declare I live beyond fear.","I declare Jesus calls me to come.","I declare His hand holds mine.","I declare the impossible bows to my obedience."]},

{"t":"The Promise Still Stands","f":"God's Word never failed me.","ref":"Numbers 23:19",
 "v":"God is not a man, that he should lie... hath he said, and shall he not do it? or hath he spoken, and shall he not make it good?",
 "s":["I waited on promises so long I was tempted to doubt them. Delay tried to convince me God had forgotten.",
 "But not one word of His ever failed. The promise still stood when my feelings did not. God cannot lie, and what He speaks He performs.",
 "If you are holding a promise that has not yet come to pass, keep holding. It still stands, and God will make it good."],
 "p":"Father, thank You that Your promise still stands. You are not a man that You should lie. Strengthen my faith in the waiting, and bring to pass every word You have spoken over my life. In Jesus' name, Amen.",
 "d":["I declare the promise still stands.","I declare God's Word never fails.","I declare what He said, He will do.","I declare delay is not denial.","I declare I hold fast to His Word."]},

{"t":"Come Forth","f":"Watching God breathe life into dead places.","ref":"John 11:43",
 "v":"And when he thus had spoken, he cried with a loud voice, Lazarus, come forth.",
 "s":["There were places in my life that smelled like the grave - finished, sealed, beyond hope. I had stopped expecting them to change.",
 "Then God called them forth. With one word He summoned life out of death. What was bound came out, and what was dead began to breathe.",
 "Hear Him calling over your dead places today: Come forth. Live again. What God calls out of the grave cannot stay buried."],
 "p":"Father, speak life over my dead places. Call them forth as You called Lazarus. Loose me from every grave-cloth and let me live again. Breathe on what I had given up. In Jesus' name, Amen.",
 "d":["I declare my dead places come forth.","I declare God breathes life into me.","I declare what was bound is loosed.","I declare I live again.","I declare resurrection over my situation."]},

{"t":"Through the Fire","f":"How trials refined my faith.","ref":"Isaiah 43:2",
 "v":"When thou walkest through the fire, thou shalt not be burned; neither shall the flame kindle upon thee.",
 "s":["I walked through fires I did not start - trials that tested everything I believed. The heat was real and the smell of smoke lingered.",
 "But I did not burn. The fire that meant to consume me only refined me. I came out with a faith purer and stronger than before.",
 "If you are in the furnace today, look again - there is a fourth man in the fire with you. You will not be burned; you will come out as gold."],
 "p":"Father, thank You that I walk through the fire and am not burned. Be the fourth man in my furnace. Refine my faith, remove the dross, and bring me out as gold for Your glory. In Jesus' name, Amen.",
 "d":["I declare I walk through the fire and am not burned.","I declare the flame will not kindle on me.","I declare trials refine my faith.","I declare I come out as gold.","I declare God is in the furnace with me."]},

{"t":"Divine Turnaround","f":"When everything changed unexpectedly.","ref":"Psalm 126:1",
 "v":"When the LORD turned again the captivity of Zion, we were like them that dream.",
 "s":["For a long time nothing seemed to move. Then, suddenly, everything did. God turned my situation around so quickly it felt like a dream.",
 "Divine turnarounds do not announce themselves; they arrive. In a moment, God can undo what years could not fix. My captivity became celebration.",
 "If you are believing for change, get ready. Your turnaround can come suddenly, and your mourning can become dancing in a day."],
 "p":"Father, thank You for divine turnarounds. Turn my captivity into freedom and my mourning into dancing. Do suddenly what years could not do. Surprise me with Your goodness. In Jesus' name, Amen.",
 "d":["I declare a divine turnaround is here.","I declare God changes things suddenly.","I declare my captivity is over.","I declare mourning turns to dancing.","I declare my breakthrough is now."]},

{"t":"Joy Came Again","f":"Discovering joy after sorrow.","ref":"Psalm 30:5",
 "v":"Weeping may endure for a night, but joy cometh in the morning.",
 "s":["Sorrow stayed for a season, and there were nights I wondered if joy would ever return.",
 "But morning came - and so did joy. God did not waste my weeping; He used it to deepen the well that joy would later fill.",
 "If you are weeping tonight, hold on until morning. Joy is not gone; it is coming. And the joy that returns after sorrow is the kind that cannot be shaken."],
 "p":"Father, thank You that joy comes in the morning. Heal my sorrow and restore my gladness. Let the joy of the Lord be my strength, deeper than any pain I have known. In Jesus' name, Amen.",
 "d":["I declare joy comes in the morning.","I declare my weeping is not wasted.","I declare gladness is restored.","I declare the joy of the Lord is my strength.","I declare unshakable joy is mine."]},

{"t":"Midnight Praise","f":"Worshiping before breakthrough.","ref":"Acts 16:25",
 "v":"And at midnight Paul and Silas prayed, and sang praises unto God: and the prisoners heard them.",
 "s":["My breakthrough often came after praise, not before it. In my darkest midnight, I learned to worship before I had a reason to.",
 "Praise in the dark is the highest form of faith - it trusts God before the answer arrives. And when I praised, chains began to break.",
 "If you are in a midnight season, lift your voice anyway. Your praise is a prison-breaker, and your breakthrough is closer than you think."],
 "p":"Father, even at midnight I will praise You. Before I see the answer, I lift my voice in faith. Shake the prison, open the doors, and loose every chain as I worship. In Jesus' name, Amen.",
 "d":["I declare I praise before my breakthrough.","I declare my midnight praise breaks chains.","I declare worship shifts the atmosphere.","I declare doors are opening.","I declare I am coming out."]},

{"t":"From Pit to Purpose","f":"God redeemed every painful season.","ref":"Genesis 50:20",
 "v":"But as for you, ye thought evil against me; but God meant it unto good... to save much people alive.",
 "s":["Like Joseph, I knew the pit before I knew the palace. Betrayal, delay, and hardship tried to bury my purpose.",
 "But God meant for good what others meant for evil. Every painful season became raw material He redeemed into purpose. Nothing was wasted.",
 "If you are in the pit, your story is not over. God specializes in turning pits into platforms and pain into purpose."],
 "p":"Father, thank You that You redeem every painful season. What was meant for evil, work for good. Lift me from the pit to the purpose You ordained, that many may be helped through my story. In Jesus' name, Amen.",
 "d":["I declare my pit becomes purpose.","I declare what was meant for evil, God means for good.","I declare nothing is wasted.","I declare I rise from the pit.","I declare my pain helps others live."]},

{"t":"Under His Shadow","f":"Finding safety in God's presence.","ref":"Psalm 91:1",
 "v":"He that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty.",
 "s":["I searched for safety in many places before I found it in His presence. The world's shelters always cracked under pressure.",
 "But under His shadow, I found a peace nothing could reach. The secret place became my refuge, my hiding place, my home.",
 "If you are looking for safety, come under His shadow. There is a covering in God's presence that no storm can penetrate."],
 "p":"Father, thank You for the safety of Your presence. Hide me under Your shadow and keep me in the secret place. Be my refuge and my fortress, my dwelling place forever. In Jesus' name, Amen.",
 "d":["I declare I dwell under His shadow.","I declare His presence is my safety.","I declare the secret place is my home.","I declare no storm can reach me there.","I declare God is my refuge."]},

{"t":"The King's Decree","f":"Walking in God's authority.","ref":"Job 22:28",
 "v":"Thou shalt also decree a thing, and it shall be established unto thee: and the light shall shine upon thy ways.",
 "s":["I once prayed as a beggar; God taught me to speak as a daughter of the King. There is authority in the words of those who know whose they are.",
 "When I learned to decree what God had already spoken, things began to shift. Heaven backs the decrees that agree with His Word.",
 "You carry the King's authority. Open your mouth and decree His promises - and watch the light shine upon your ways."],
 "p":"Father, thank You for the authority You have given me as Your child. Teach me to decree Your Word in faith. Establish the things I declare in agreement with You, and let light shine upon my ways. In Jesus' name, Amen.",
 "d":["I declare I walk in God's authority.","I declare what I decree is established.","I declare I speak as a child of the King.","I declare Heaven backs His Word in my mouth.","I declare light shines upon my ways."]},

{"t":"Favored, Yet I Still Had to Fight","f":"Looking back over the journey and pointing readers toward hope.","ref":"Joshua 1:9",
 "v":"Be strong and of a good courage; be not afraid... for the LORD thy God is with thee whithersoever thou goest.",
 "s":["I have been favored by God - and I still had to fight. Favor did not exempt me from the battle; it carried me through it.",
 "Looking back over the whole journey, I see a thread of grace running through every fight. God was with me in the loss, the healing, the waiting, and the rising.",
 "If you are favored and still fighting, do not be discouraged. Favor and warfare can share the same season. Be strong and courageous - the God who brought me through will bring you through too. Keep walking on the water."],
 "p":"Father, thank You for favor that carried me through every fight. Make me strong and courageous. As I look back, I trust You for what is ahead. Be with me wherever I go, and let my journey point others to hope. In Jesus' name, Amen.",
 "d":["I declare I am favored by God.","I declare favor carries me through the fight.","I declare I am strong and courageous.","I declare God is with me wherever I go.","I declare my story points others to hope."]},
]

# ---- Loretta's own testimony reflections (override Chapter Story) ----
OV={
2:("Jeremiah 1:5","Before I formed thee in the belly I knew thee; and before thou camest forth out of the womb I sanctified thee, and I ordained thee a prophet unto the nations.",
 ["Every testimony has a beginning, and mine began long before I understood God's purpose for my life.",
  "Before I ever knew the battles I would face, before the surgeries, the losses, the tears, and the victories, God already knew my name. He knew every step I would take and every storm I would survive. Nothing in my life has ever surprised Him.",
  "When I look back to where my story began, I don't simply see people or places - I see the hand of God. I see His protection even when I didn't recognize it. I see His mercy covering me through seasons that could have destroyed me. I see His faithfulness carrying me when I wasn't strong enough to carry myself.",
  "There were chapters of my life I didn't understand while I was living them. Some questions remained unanswered for years. Yet with time, I realized that God was writing a story far greater than the one I could see.",
  "Today, I stand as living proof that God finishes what He starts. My beginning may have looked ordinary, and my journey has certainly included pain, but His purpose has been extraordinary.",
  "If God has been faithful from the beginning of my story, He will be faithful in yours as well. Your beginning does not determine your destiny. God's purpose does."]),
3:(None,None,["I learned that God often places people in our lives to encourage, protect, and strengthen us. Their presence reminds us that we were never meant to walk alone."]),
4:(None,None,["There were seasons when I felt abandoned, but God proved He would never leave me. When others walked away, He drew closer."]),
5:(None,None,["Some of my darkest days became the place where I discovered God's greatest faithfulness. Even in the valley, His light never stopped shining."]),
6:(None,None,["Through surgeries, sickness, and uncertainty, God preserved my life. Every breath became evidence that He still had purpose for me."]),
7:(None,None,["Healing didn't happen overnight. God taught me that progress is still a miracle and that every step forward is worth celebrating."]),
8:(None,None,["God opened doors no person could open. He taught me that His timing is always perfect."]),
9:(None,None,["Before God could use me publicly, He wanted my heart completely surrendered to Him. My identity was found in Christ alone."]),
10:(None,None,["Even when life tried to pull me under, God's promises remained above every storm. His Word never sank."]),
11:(None,None,["God transformed my pain into purpose and called me to help others discover His love and hope."]),
12:(None,None,["The wilderness wasn't punishment - it was preparation. God supplied everything I needed while teaching me to trust Him."]),
13:(None,None,["Looking back, I now understand that suffering was never the end of my story. God used every trial to strengthen me."]),
14:(None,None,["Faith begins with obedience. I learned that God often reveals the next step only after we take the first one."]),
15:(None,None,["Storms came, but Jesus remained in the boat with me. His presence gave me peace even before circumstances changed."]),
16:(None,None,["Some of God's greatest blessings arrived in ways I never expected. His plans were always better than mine."]),
17:(None,None,["Whenever I focused on fear, I sank. Whenever I fixed my eyes on Christ, I found strength to keep walking."]),
18:(None,None,["Many battles came against me, but God's promises stood stronger than every attack."]),
19:(None,None,["The places where I thought everything had ended became places of resurrection. God brought life where I expected loss."]),
20:(None,None,["God called me beyond comfort into complete dependence upon Him. Faith became my bridge over impossible situations."]),
21:(None,None,["Time never cancels God's promises. What He spoke over my life remained true through every season."]),
22:(None,None,["God called me out of places where fear, disappointment, and pain had tried to keep me bound."]),
23:(None,None,["The fire did not destroy me - it refined me. I came out stronger, wiser, and closer to God."]),
24:(None,None,["When I thought all hope was gone, God changed everything. One moment in His presence can redirect an entire life."]),
25:(None,None,["God restored laughter where there had been tears and reminded me that joy truly comes in the morning."]),
26:(None,None,["Some of my greatest victories began when I chose to worship before I saw the breakthrough."]),
27:(None,None,["The painful places of my life became the foundation for the ministry God entrusted to me."]),
28:(None,None,["God became my refuge and safe place. His presence sheltered me through every storm."]),
29:(None,None,["I learned to live according to God's Word instead of the world's opinions. His decree over my life became my confidence."]),
30:(None,None,["Favor does not mean a life without battles. It means God walks with us through every battle until the victory is complete."]),
}
for i,(ref,v,s) in OV.items():
    if ref: CH[i-1]['ref']=ref
    if v: CH[i-1]['v']=v
    CH[i-1]['s']=s

def bg(c,top,bottom):
    for i in range(80):
        t=i/80
        c.setFillColorRGB(top.red+(bottom.red-top.red)*t,top.green+(bottom.green-top.green)*t,top.blue+(bottom.blue-top.blue)*t)
        c.rect(0,H-(i+1)*H/80,W,H/80+1,fill=1,stroke=0)

DREW=[]
def head(c,txt,y,color=TEAL):
    DREW.append(txt)
    c.setFont('Times-Bold',16); c.setFillColor(color); c.drawString(1*inch,y,txt)
    c.setStrokeColor(GOLD); c.setLineWidth(1.5); c.line(1*inch,y-6,W-1*inch,y-6); return y-26

def wrap(c,text,x,y,width,font='Times-Roman',size=11.5,lead=16,color=INK):
    c.setFont(font,size); c.setFillColor(color); cpl=int(width/(size*0.5))
    for para in text.split('\n'):
        if not para.strip(): y-=lead*0.6; continue
        for line in textwrap.wrap(para,cpl): c.drawString(x,y,line); y-=lead
        y-=lead*0.35
    return y

def lined(c,y,n=14):
    c.setStrokeColor(HexColor('#cdd6df')); c.setLineWidth(0.7)
    for i in range(n): c.line(1*inch,y-i*0.42*inch,W-1*inch,y-i*0.42*inch)
    return y-n*0.42*inch

def slug(t): return re.sub(r'[^A-Za-z0-9 ]','',t).strip().replace(' ','_')[:42]

import math
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

# Scene presets: sky_top, sky_bottom(=water surface), water_deep, celestial
SCENE={
 'dawn':  ('#f6c177','#e8835a','#0a3a5c','sun'),
 'storm': ('#243447','#33506b','#08203a','bolt'),
 'night': ('#0a1733','#13294a','#06182e','moon'),
 'open':  ('#bfe3f5','#5aa6d6','#0a3a5c','glow'),
 'glory': ('#21385c','#2f5588','#0a2540','rays'),
}
# per-chapter scene assignment (matched to theme)
CHSCENE=['glory','dawn','open','night','night','dawn','dawn','open','glory','open',
 'open','dawn','dawn','open','storm','glory','open','storm','glory','open',
 'open','glory','storm','dawn','dawn','night','glory','night','glory','glory']

def hx(s): return HexColor(s)

def draw_cover(c, idx, ch):
    sky_t,sky_b,deep,cel=SCENE[CHSCENE[idx-1]]
    st,sb,dp=hx(sky_t),hx(sky_b),hx(deep)
    waterline=H*0.42
    # sky gradient (top -> waterline)
    steps=60
    for i in range(steps):
        t=i/steps; y=H-i*((H-waterline)/steps)
        c.setFillColorRGB(st.red+(sb.red-st.red)*t, st.green+(sb.green-st.green)*t, st.blue+(sb.blue-st.blue)*t)
        c.rect(0,y-((H-waterline)/steps)-1,W,(H-waterline)/steps+2,fill=1,stroke=0)
    # water gradient (waterline -> bottom)
    for i in range(steps):
        t=i/steps; y=waterline-i*(waterline/steps)
        c.setFillColorRGB(sb.red+(dp.red-sb.red)*t, sb.green+(dp.green-sb.green)*t, sb.blue+(dp.blue-sb.blue)*t)
        c.rect(0,y-(waterline/steps)-1,W,(waterline/steps)+2,fill=1,stroke=0)
    # celestial element
    cx=W*(0.30+0.12*((idx%4)))  # vary position per chapter
    if cel=='sun':
        c.setFillColor(hx('#ffe6a8')); c.circle(cx,waterline+1.2*inch,0.7*inch,fill=1,stroke=0)
        c.setFillColor(hx('#fff2cf')); c.setFillAlpha(0.25); c.circle(cx,waterline+1.2*inch,1.3*inch,fill=1,stroke=0); c.setFillAlpha(1)
    elif cel=='moon':
        c.setFillColor(hx('#e8eef7')); c.circle(cx,H-1.9*inch,0.55*inch,fill=1,stroke=0)
        c.setFillColor(sb); c.circle(cx+0.22*inch,H-1.78*inch,0.5*inch,fill=1,stroke=0)
        c.setFillColor(white)
        import random; random.seed(idx)
        for _ in range(18+idx%10):
            c.circle(random.uniform(0.3*inch,W-0.3*inch), random.uniform(waterline+0.4*inch,H-0.4*inch), random.uniform(0.4,1.4),fill=1,stroke=0)
    elif cel=='glow':
        c.setFillColor(hx('#fff6df')); c.setFillAlpha(0.5); c.circle(cx,waterline+0.2*inch,1.6*inch,fill=1,stroke=0); c.setFillAlpha(1)
        c.setFillColor(hx('#ffffff')); c.circle(cx,waterline+0.2*inch,0.5*inch,fill=1,stroke=0)
    elif cel=='rays':
        c.setFillColor(hx('#f4d77e')); c.setFillAlpha(0.18)
        for k in range(9):
            ang=math.radians(200+k*16); x2=cx+math.cos(ang)*9*inch; y2=(H-0.2*inch)+math.sin(ang)*9*inch
            p=c.beginPath(); p.moveTo(cx-0.6*inch,H-0.2*inch); p.lineTo(cx+0.6*inch,H-0.2*inch); p.lineTo(x2,y2); p.close(); c.drawPath(p,fill=1,stroke=0)
        c.setFillAlpha(1)
    elif cel=='bolt':
        c.setStrokeColor(hx('#dfe9f2')); c.setLineWidth(2.2); c.setFillColor(hx('#dfe9f2'))
        bx=cx; by=H-1.4*inch
        pts=[(bx,by),(bx-0.18*inch,by-0.5*inch),(bx+0.05*inch,by-0.5*inch),(bx-0.16*inch,by-1.1*inch)]
        c.lines([(pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1]) for i in range(len(pts)-1)])
    # wave bands over water
    band_cols=['#2b6f9e','#205a86','#16466b','#0e3354']
    for b in range(4):
        base=waterline-0.15*inch-b*0.55*inch
        amp=0.10*inch+0.05*inch*((idx+b)%3)
        ph=idx*0.6+b
        p=c.beginPath(); p.moveTo(0,base+amp*math.sin(ph))
        x=0
        while x<=W:
            p.lineTo(x, base+amp*math.sin(x/55.0+ph)); x+=10
        p.lineTo(W,0); p.lineTo(0,0); p.close()
        col=hx(band_cols[b]); c.setFillColor(col); c.setFillAlpha(0.55); c.drawPath(p,fill=1,stroke=0); c.setFillAlpha(1)
    # legibility panel behind title
    c.setFillColor(hx('#06182e')); c.setFillAlpha(0.35); c.rect(0.7*inch,H-4.7*inch,W-1.4*inch,2.9*inch,fill=1,stroke=0); c.setFillAlpha(1)
    # branding
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold',13); c.drawCentredString(W/2,H-1.15*inch,"HEAVENLY HANDS DIVINE")
    c.setFillColor(white); c.setFont('Helvetica',10.5); c.drawCentredString(W/2,H-1.42*inch,"WALK ON WATER SERIES")
    c.setStrokeColor(GOLD); c.setLineWidth(1); c.line(W/2-1.2*inch,H-1.62*inch,W/2+1.2*inch,H-1.62*inch)
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold',12); c.drawCentredString(W/2,H-2.3*inch,f"CHAPTER {NUMWORD[idx].upper()}")
    c.setFillColor(white); c.setFont('Times-Bold',29)
    for j,seg in enumerate(textwrap.wrap(ch['t'],24)):
        c.drawCentredString(W/2,H-3.0*inch-j*0.44*inch,seg)
    c.setFillColor(hx('#e8d9a8')); c.setFont('Times-Italic',12); c.drawCentredString(W/2,H-4.25*inch,ch['f'])
    c.setFillColor(hx('#dbe9f5')); c.setFont('Times-Italic',11); c.drawCentredString(W/2,H-4.55*inch,ch['ref'])
    c.setFillColor(GOLD); c.setFont('Times-Italic',15); c.drawCentredString(W/2,1.15*inch,'Loretta "Lolo" Hall')

def draw_qr(c, url, x, y, size):
    qr=QrCodeWidget(url); b=qr.getBounds(); w=b[2]-b[0]; h=b[3]-b[1]
    d=Drawing(size,size,transform=[size/w,0,0,size/h,0,0]); d.add(qr); renderPDF.draw(d,c,x,y)

os.makedirs('wow_pdfs',exist_ok=True)
SECTIONS={}
for idx,ch in enumerate(CH,1):
    DREW.clear()
    fn=f"wow_pdfs/WOW{idx:02d}_{slug(ch['t'])}.pdf"
    c=canvas.Canvas(fn,pagesize=letter); PN=[0]
    def foot():
        PN[0]+=1; c.setFont('Helvetica',8); c.setFillColor(SOFT)
        c.drawCentredString(W/2,0.5*inch,f"Heavenly Hands Divine  •  Walk On Water Series  •  Chapter {idx}  •  {PN[0]}")
    # COVER (unique themed water scene per chapter)
    draw_cover(c, idx, ch); c.showPage()
    # WELCOME
    y=head(c,"Welcome",H-1.1*inch)
    wrap(c,f'Hello, and welcome.\n\nBefore you read another word, take a breath and invite God into this '
         f'moment with you. This chapter - "{ch["t"]}" - is not just something to read; it is a place to '
         f'meet Him.\n\nCome with an open heart. Let Him speak to the very thing you are carrying today.\n\n'
         f'With love and faith,\nLolo',1*inch,y,W-2*inch); foot(); c.showPage()
    # KEY SCRIPTURE
    y=head(c,"Key Scripture",H-1.1*inch)
    y=wrap(c,'"'+ch['v']+'"',1*inch,y,W-2*inch,font='Times-Italic',size=13.5,lead=19,color=NAVY)
    c.setFont('Times-Bold',12); c.setFillColor(GOLD); c.drawString(1*inch,y,ch['ref']); y-=24
    y=wrap(c,f'Why this scripture matters: This is the promise beneath "{ch["t"]}." Let it anchor you as '
           f'you read - {ch["f"][0].lower()+ch["f"][1:]}',1*inch,y,W-2*inch); foot(); c.showPage()
    # CHAPTER STORY (auto-paginate)
    y=head(c,"Chapter Story - My Testimony",H-1.1*inch); c.setFont('Times-Roman',11.5); c.setFillColor(INK)
    cpl=int((W-2*inch)/(11.5*0.5))
    for para in ch['s']:
        for line in textwrap.wrap(para,cpl):
            if y<1.0*inch: foot(); c.showPage(); y=head(c,"Chapter Story (cont.)",H-1.1*inch); c.setFont('Times-Roman',11.5); c.setFillColor(INK)
            c.drawString(1*inch,y,line); y-=16.5
        y-=8
    if y<1.2*inch: foot(); c.showPage(); y=H-1.3*inch
    c.setFont('Times-Italic',12); c.setFillColor(GOLD); c.drawString(1*inch,y,'With love and faith,')
    c.setFont('Times-BoldItalic',13); c.drawString(1*inch,y-0.26*inch,'Loretta "Lolo" Hall')
    c.setFont('Times-Italic',10.5); c.setFillColor(SOFT); c.drawString(1*inch,y-0.48*inch,'Founder, Heavenly Hands Divine')
    foot(); c.showPage()
    # FROM THE BOOK (up to 3 inserts)
    ins=ch.get('ins',[])
    if ins:
        y=head(c,"From the Walk On Water Book",H-1.1*inch)
        for q in ins[:3]:
            lines=textwrap.wrap('"'+q+'"', int((W-2.8*inch)/(13*0.5)))
            bh=len(lines)*20+34
            if y-bh<1.2*inch: foot(); c.showPage(); y=head(c,"From the Walk On Water Book (cont.)",H-1.1*inch)
            c.setFillColor(HexColor('#f3f7fb')); c.rect(1*inch,y-bh,W-2*inch,bh,stroke=0,fill=1)
            c.setStrokeColor(GOLD); c.setLineWidth(3); c.line(1*inch,y-bh,1*inch,y)
            yy=y-24; c.setFont('Times-Italic',13); c.setFillColor(NAVY)
            for ln in lines: c.drawCentredString(W/2,yy,ln); yy-=20
            c.setFont('Times-Italic',10); c.setFillColor(GOLD); c.drawRightString(W-1.3*inch,y-bh+12,'— Lolo')
            y=y-bh-0.45*inch
        foot(); c.showPage()
    # REFLECTION
    y=head(c,"Reflection",H-1.1*inch)
    for q in ["What is God saying to me?","What fear do I need to release?","What promise do I need to believe?","What step of faith am I being asked to take?"]:
        c.setFont('Times-Bold',12); c.setFillColor(NAVY); c.drawString(1*inch,y,"•  "+q); y-=0.2*inch; y=lined(c,y,2); y-=0.12*inch
    foot(); c.showPage()
    # PRAYER
    y=head(c,"Prayer",H-1.1*inch); wrap(c,ch['p'],1*inch,y,W-2*inch); foot(); c.showPage()
    # DECLARATION
    y=head(c,"Declaration",H-1.1*inch)
    for d in ch['d']: c.setFont('Times-Italic',13); c.setFillColor(TEAL); c.drawString(1*inch,y,'"'+d+'"'); y-=0.33*inch
    foot(); c.showPage()
    # ACTION STEPS
    y=head(c,"Action Steps",H-1.1*inch)
    for a in [f"Read {ch['ref']} out loud every morning this week.","Pray for someone walking through a similar season.",f'Journal what "{ch["t"]}" stirs in your heart.',"Worship for 15 minutes with open hands.","Take one step of faith this week."]:
        c.setFont('Times-Roman',12); c.setFillColor(INK); c.drawString(1*inch,y,"☐  "+a); y-=0.34*inch
    foot(); c.showPage()
    # JOURNAL
    y=head(c,"Journal - What God Spoke to Me",H-1.1*inch); lined(c,y,16); foot(); c.showPage()
    # PRAYER NOTES
    y=head(c,"Prayer Notes",H-1.1*inch); c.setFont('Times-Bold',11); c.setFillColor(SOFT)
    c.drawString(1*inch,y,"Prayer Request"); c.drawString(4.2*inch,y,"Date"); c.drawString(5.5*inch,y,"Answered / Praise")
    y-=0.1*inch; lined(c,y,16); foot(); c.showPage()
    # RELATED PRODUCTS
    y=head(c,"Related Products",H-1.1*inch)
    y=wrap(c,"Continue your Walk On Water journey with these Heavenly Hands Divine companions:",1*inch,y,W-2*inch); y-=0.2*inch
    for p in ["Matching Prayer Scroll","Selah Victory Figurine","Divina Wings Apparel","Walk On Water Study Guide","Faith Journal"]:
        c.setFont('Times-Bold',12); c.setFillColor(NAVY); c.drawString(1.2*inch,y,"✦  "+p); y-=0.34*inch
    foot(); c.showPage()
    # CLOSING BLESSING
    y=head(c,"Closing Blessing",H-1.1*inch)
    wrap(c,'"May the God who called you upon the waters strengthen your faith, calm every storm before you, '
         'and remind you that His hand has never left yours. Continue to walk in faith, knowing that He who '
         'began a good work in you will carry it to completion."',1*inch,y,W-2*inch,font='Times-Italic',size=14,lead=21,color=NAVY)
    c.setFont('Times-Italic',13); c.setFillColor(GOLD); c.drawString(1*inch,y-2.0*inch,'— Loretta "Lolo" Hall')
    foot(); c.showPage()
    # BACK COVER
    bg(c,HexColor('#1b6ca8'),HexColor('#0a2540'))
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold',16); c.drawCentredString(W/2,H-2*inch,"HEAVENLY HANDS DIVINE")
    c.setFillColor(white); c.setFont('Times-Italic',12); c.drawCentredString(W/2,H-2.4*inch,"Faith Over Fear")
    c.setFont('Helvetica',11); c.setFillColor(HexColor('#dbe9f5'))
    for i,t in enumerate(["www.heavenlyhandsdivine.com","Shop: heavenlyhandsdivine.com/store","@HeavenlyHandsDivine",f"Walk On Water Series — Chapter {idx}"]):
        c.drawCentredString(W/2,H-3.4*inch-i*0.3*inch,t)
    qsize=1.25*inch
    c.setFillColor(white); c.rect(W/2-qsize/2-6,2.2*inch-6,qsize+12,qsize+12,fill=1,stroke=0)
    draw_qr(c, f"https://www.heavenlyhandsdivine.com/wow/chapter-{idx}", W/2-qsize/2, 2.2*inch, qsize)
    c.setFont('Helvetica',8); c.setFillColor(white); c.drawCentredString(W/2,2.0*inch,"Scan: prayer • worship • teaching • video")
    c.setFont('Helvetica',8); c.setFillColor(HexColor('#9fc1de')); c.drawCentredString(W/2,0.9*inch,"© 2026 Heavenly Hands Divine. All rights reserved.")
    c.showPage(); c.save()
    SECTIONS[idx]=list(DREW)

# ---- AUDIT ----
REQ=["Welcome","Key Scripture","Chapter Story","Reflection","Prayer","Declaration","Action Steps","Journal","Prayer Notes","Related Products","Closing Blessing"]
rows=["Chapter,Title,Sections_Present,All_Required_OK"]
allok=True
for idx,ch in enumerate(CH,1):
    drew=SECTIONS[idx]
    present=[r for r in REQ if any(d.startswith(r) for d in drew)]
    ok=len(present)==len(REQ)
    allok=allok and ok
    rows.append(f'{idx},"{ch["t"]}",{len(present)}/{len(REQ)},{"YES" if ok else "NO -> missing "+str([r for r in REQ if r not in present])}')
open('WOW_AUDIT.csv','w').write("\n".join(rows)+"\n")
print("built", len(CH), "chapter PDFs")
print("AUDIT: every chapter has all", len(REQ), "required sections:", allok)
