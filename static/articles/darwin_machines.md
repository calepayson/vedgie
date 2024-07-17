# Darwin Machines

I'm writing this because I've been obsessed with the theory of a Darwin Machine for nearly a year now and I haven't met anyone else who has heard of it.

This is my attempt to summarize and share the theory that William Calvin laid out in "The Cerebral Code". If you haven't read it and are interested in how the brain works or AI/ML you should order a copy right now. I'm going to do the book no justice but hopefully, if you haven't already ordered the book, the rest of this post will convince you to read it.

If you, or anyone you know, is interested in these ideas or wants to build/is building a Darwin Machine, please reach out. My email is calepayson(at)mac.com. 

## First a Little Background

### On Evolution:

Near the end of his career Schrodinger wrote a book, "What is Life?", that provides a great lens through which to view biology: Life is unnatural... If you're a physicist.

One of the defining pillars of physics is the second law of thermodynamics. Energy hates being concentrated. Yet here we are, squishy bags of water and energy suspended a few feet above the ground. It's a bit weird.

Schrodinger decided the only way that life was possible was if it led to more entropy throughout the system. Like a tornado, life is a pocket of order that sows disorder. It lives so long as it pays the entropy tax.

To anthropomorphize a bit, The Universe is trying to maximize entropy but it has a near infinite "problem space". One algorithm it has found to solve this problem is evolution. To butcher a computer science phrase, I believe that evolution is the "best case runtime" when trying to find increasingly valid solutions to a near infinite problem space.

Essentially, biology uses evolution because it is the best way to solve the problem of prediction (survival/reproduction) in a complex world.

### On Constraints:

I love constraints in science because they can give us hope for a theory before it has been worked out. For example, before we knew what genetic material was, we knew it had to fit in cells, be chemically stable, and had to be capable of making high fidelity copies of itself. It took four years after Watson and Crick discovered the double helix for us to prove it was genetic material but we knew their discovery held promise because it fit within the constraints.

I see a few constraints governing how the brain works. 

First, and most importantly, the brain is also faced with a near infinite problem space. There are trillions of behaviors, only some of which are "fit" for any given scenario. Any theory of intelligence should explain how the brain solves this in the most efficient manner possible.

The other constraints are based on a few studies and observations that seem important.

Karl Lashley showed that memory is massively parallel and, contrary to the idea of a "grandmother cell", is not stored in a single location.

David Eagleman showed that other brain functions in the brain like perception are also massively parallel. He dubbed this the "Mr. Potato Head" theory because no matter where you "plug in" sensory input, your brain tends to figure out what to do with it. Plug some eyes into the olfactory cortex and a nose into the visual cortex and the brain will keep right on trucking.

Two additional things to add:

Brain patterns are spatio-temporal patterns. If I turn off cell firings, say with anesthesia, you lose your train of thought.:

But they store those patterns spatially. When you come out of anesthesia, you're still you.

Think of this like RAM vs. Disk.

### On Brains

If you were to flatten out the brain on a table you would notice two things.

First, if you look at a cross-section of the brain (eye-level with the table), the brain is divided into ~6 layers. This layering forms the dominant narrative of how intelligence may work and is the basis for deep neural nets. The idea is, stimulus is piped into the "top" layer and filters down to the bottom layer, with each layer picking up on more and more abstract concepts. Three Blue One Brown does a good job of articulating this idea in a [video](https://youtu.be/aircAruvnKk?si=MMZ_O7NATm38f_DT&t=332).

Second, if you look down on the brain from above, the brain is divided into columns. The smallest unit of these are minicolumns, bundles of 80-120 neurons that run perpendicular to the layers of the brain, from the "top" to the "bottom" (or vice versa, it doesn't matter). These minicolumns can then be grouped into cortical columns, which can be thought of as roughly hexagonal bundles of minicolumns, also running perpendicular to the layers of the brain.

And that's about it. The brain is incredibly, wonderfully, complex. The neocortex, the new bit that we think is important for intelligence, is insanely complex too. And it's also basically a crumpled up sheet with the structure described above. At least that's the level of abstraction we'll be working with.

From the perspective of a bystander, modern machine learning seems to believe that the recipe for more intelligence is adding more layers. But based upon the homogeneity of neocortex it seems that, in biology, the recipe for more intelligence is adding more columns. A rat has the same number of layers as a chimp as a human, but the surface area of a rat's neocortex, a proxy for the number of columns, is less than a chimp which is less than a human.

To prevent confusion, I'm saying that adding more columns is the recipe for more "animal intelligence. "Human intelligence" is different than animal intelligence owing to our capacity for high fidelity imitation. I'll write more on this in the future.

# On Darwin Machines

If modern ML explains intelligence with layers, the theory of a Darwin Machine explains evolution with columns.

As a reminder, a theory should satisfy the following:

1. Implements an efficient algorithm to search a near infinite problem space.

2. Both memory and processing are massively parallel.

3. Computation uses spatio-temporal patterns.

4. But memory is spatial.

The theory of Darwin Machines developed by William Calvin proposes that the brain, like life, implements evolution to search a near infinite problem space.

Calvin believes that minicolumns are the arena for this evolution. Sensory inputs hit the brain, visual input in one area, olfactory in another, etc. and trigger specific firing patterns in the minicolumns. Imagining the surface of the brain laid flat on a table, we can look down on it and see these columns lighting up, as if with Morse Code messages. These messages then propagate across the surface area of the brain, competing with conflicting messages to take over the greatest surface area.

After some period of time a winner is chosen, likely the message that controls the greatest surface area, the greatest number of minicolumns. When this happens, the winning minicolumns are rewarded, likely prompting them to encode a tendency for that firing pattern into their structure.

Before we go deeper let's pause and notice that this theory satisfies all our constraints. It implements the "best case runtime" algorithm for predicting "valid" solutions to a complex problem space. It is massively parallel with computation and storage happening between and within individual minicolumns. The calculation is done with a spatiotemporal "Morse Code" message. But storage is performed by changing the spatial relationships within a minicolumn so that the message is more easily triggered in the future.

This all seems so simple. There are only so many firing patterns a minicolumn can have within some reasonable clock speed yet there is a practically infinite range of thought. How does the Darwin Machine theory explain that? This brings us to cortical columns.

Minicolumns communicate with each other using axons, basically wires. Some of these wires connect neighboring minicolumns but many reach further, skipping roughly ten minicolumns before connecting. These connections result in a triangular array of connected minicolumns with large gaps of unconnected minicolumns in between. Well, not really unconnected, each of these are connected to their own triangular array.

Looking down on the brain again, we can imagine projecting a pattern of equilateral triangles - like a fishing net - over the surface. Each vertex in the net will land on a minicolumn within the same network, leaving holes over minicolumns that don't belong to that network. If we were to project nets over the network until every minicolumn was covered by a vertex we would project 50-100 nets.

A cortical column is made up of 50-100 minicolumns. You can think of a cortical column as a hexagon containing one minicolumn from each network.

Cortical columns allow for the complexity that minicolumns alone couldn't provide. Each one can encode somewhere between n^50 and n^100 unique patterns where n is the number of patterns that a minicolumn can encode. Even if minicolumns only had two states, this would provide us with the building blocks for a massive range of thoughts.

With all this in mind we can tell the story of how a Darwin Machine works.

Sensory input comes in and causes minicolumns to fire in certain patterns. The resulting pattern is influenced by the input and the "tendencies" of the minicolumn that have been spatially encoded over time. Each firing pattern, each message, competes with other messages from minicolumns within its network. Through this competition each network settles on the most fit message, the message that best correlates with sensory input and the tendencies of its minicolumns.

At the cortical column level, the message from each network is read. Here I'll steal one of Calvin's metaphors: Each message is like an individual instrument in a band or orchestra. It encodes some bit of information but it's the amalgamation that is important. "Super Freak" and "U Can't Touch This" are two very different songs despite having the same bass and piano riff. Likewise, two different thoughts or concepts can be made of many of the same minicolumn firing patterns.

Eventually a winner is chosen, possibly by finding the "song" playing on the most cortical columns, and learning happens. The winning cortical columns are rewarded, somehow leading to their minicolumns encoding a tendency towards the message they were transmitting. These minicolumns will "remember" that firing pattern and are more likely to produce it in the future.

A Darwin Machine uses evolution to produce intelligence. It relies on the same insight that produced biology: That evolution is the best algorithm for predicting valid "solutions" within a near infinite problem space.

## Some Speculation

### On Advantages

I believe the theory of Darwin Machines illuminates a path to solving one of the biggest problems in AI right now. Current algorithms are great at system one thinking, quick thoughts, intuition. But they are not capable of system two thinking, deep thinking, where time spent on the problem correlates with a better answer.

The evolutionary approach of Darwin Machines seems to allow for the possibility of both. System one thinking would only run the competition for a short time, relying on the tendencies encoded in minicolumns to provide a quick and "good enough" behavior. System two thinking would let the competition run longer, allowing evolution to play out, leading to novel and "more fit" thoughts.

### On Creativity

Many people believe that, in biology, point mutations lead to the change necessary to drive novelty in evolution. This is rarely the case. Point mutations are usually disastrous and every organism I know of does everything in its power to minimize them. Think, for every one beneficial point mutation, there are thousands that don't have any effect, and hundreds that cause something awful like cancer. If you're building a skyscraper, having one in a hundred bricks be laid with some variation is not a good thing.

Instead Biology relies on recombination. Swap one beneficial trait for another and there's a much smaller chance you'll end up with something harmful and a much higher chance you'll end up with something useful.

Recombination is the key to the creativity of evolution, and Darwin Machines harness it. A complex thought such as a memory of your grandmother is likely represented in a cortical column as a specific combination of spatiotemporal firing patterns within its minicolumns. But let's say you need to think of someone else's grandmother. The individual firing patterns that code for a grandmother probably remain, but the ones that code information specific to yours are likely swapped out for patterns corresponding to the new grandmother.

Maybe you're interested in bird watching and see a new bird. Your brain likely uses recombination to form the thought representing this bird. Maybe you've never seen a flamingo before. Some networks of minicolumns might identify features similar to a parrot you saw once, perhaps the pink coloring. Some might light up to say that the beak looks a bit like a toucan's. Others might propagate a message suggesting it's the size of an ostrich. etc. All these different messages can then mix together and our brain can store this unique combination as a flamingo.

Or in the other direction. When you're thinking hard about a question, you could let your mind wander a little (isn't that when all the good ideas hit us?). Maybe the act of mind wandering lets some message within the cortical column get exchanged for another. And WHAM! A new idea, a possible solution.

This is all speculation but I hope you can see the beauty of the Darwin Machine framework. I've been immersed in neuroscience for about four years now and nothing I've come across comes close to the breadth of explanation that this theory promises if born out in experiments.

### On Implementation

Neural nets are great at intuition. They can take a seemingly infinite number of inputs and encode them into a relatively small space. Then, when prompted they can spit out something that is ~95% correct.

I suspect minicolumns and neural nets are, to a large extent, functionally equivalent. I'm trying small neural nets implemented in an array instead of one lone massive neural net. If it takes them one cycle to process an input pattern to an output pattern, then every cycle they should take a sensory input, and the input from adjacent neural nets in their array, and produce an output that, overtime, synchronizes throughout the array. I would love any advice, from anyone, about how to cunduct my own research and subsequent academics (if necessary) in order to work in this space.

I hope you find this idea as exciting as I do.
