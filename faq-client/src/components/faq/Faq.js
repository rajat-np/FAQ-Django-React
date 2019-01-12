import React from 'react';
import './styles.css';
import {
    Accordion,
    AccordionItem,
    AccordionItemTitle,
    AccordionItemBody,
} from 'react-accessible-accordion';

 
const Faq = (props) => (
    <Accordion className="body">
        <h3 className = "text-center">Frequently asked questions</h3>
        {props.data.map((item,key) => (<AccordionItem>
                                <AccordionItemTitle className = "accordion__title">
                                    <h3 className="u-position-relative">{item.question}
                                    <div className="accordion__arrow" role="presentation"/>
                                    </h3>
                                </AccordionItemTitle>
                                <AccordionItemBody>
                                    <p>{item.answer}</p>
                                </AccordionItemBody>
                            </AccordionItem>))}
    </Accordion>
);
 
export default Faq;