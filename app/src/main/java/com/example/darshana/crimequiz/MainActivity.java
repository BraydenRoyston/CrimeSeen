package com.example.darshana.crimequiz;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.darshana.geoquiz.R;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private Button mTrueButton;
    private Button mFalseButton;
    private Toast mycorrecttoast;
    private Button mNextButton;
    private TextView mQuestionTextView;
    private int number_correct =0;

    private Question[] mQuestionBank = new Question[]{
            new Question(R.string.question_metropolitan, true),
            new Question(R.string.question_police, false),
            new Question(R.string.question_toronto, true),
            new Question(R.string.question_homocides, true),
            new Question(R.string.question_canada, false),
            new Question(R.string.question_curfew, true),
            new Question(R.string.question_baystreet, true),
            new Question(R.string.question_trafficking, true),
            new Question(R.string.question_islington, true),
            new Question(R.string.question_hillcrest, false),
            new Question(R.string.question_stolencar, false),
            new Question(R.string.question_caledon, false),
            new Question(R.string.question_gta, false),
            new Question(R.string.question_kingswaysouth, false),
            new Question(R.string.question_hatecrime, true),
            new Question(R.string.question_burlington, true)

    };


    private int mCurrentIndex;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mycorrecttoast = Toast.makeText(MainActivity.this, "Correct", Toast.LENGTH_SHORT);
        mycorrecttoast.setGravity(Gravity.CENTER | Gravity.CENTER, 0, 450);
        mQuestionTextView = (TextView) findViewById(R.id.question_text_view);
        mTrueButton = (Button) findViewById(R.id.true_button);
        LayoutInflater li=getLayoutInflater();
        View layout = li.inflate(R.layout.customtoast, (ViewGroup)findViewById(R.id.custom));
        final Toast visual_toast = new Toast(getApplicationContext());
        visual_toast.setDuration(Toast.LENGTH_LONG);
        visual_toast.setGravity(Gravity.CENTER, 0, 600);
        visual_toast.setView(layout);
        LayoutInflater li_incorrect=getLayoutInflater();
        View layout_incorrect = li_incorrect.inflate(R.layout.incorrect, (ViewGroup)findViewById(R.id.custom));
        final Toast incorrect_toast = new Toast(getApplicationContext());
        incorrect_toast.setDuration(Toast.LENGTH_LONG);
        incorrect_toast.setGravity(Gravity.CENTER, 0, 600);
        incorrect_toast.setView(layout_incorrect);


        mTrueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mQuestionBank[mCurrentIndex].isAnswerTrue())
                {
                    visual_toast.show();
                }
                else
                {
                    incorrect_toast.show();
                }

            }
        });
        mFalseButton = (Button) findViewById(R.id.false_button);
        mFalseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!mQuestionBank[mCurrentIndex].isAnswerTrue())
                {
                    visual_toast.show();
                }
                else
                {
                    incorrect_toast.show();
                }
            }
        });
        mNextButton = (Button) findViewById(R.id.next_button);
        mNextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mCurrentIndex = (mCurrentIndex + 1) % mQuestionBank.length;
                updateQuestion();
            }
        });
        updateQuestion();
    }
        private void updateQuestion(){
            int question = mQuestionBank[mCurrentIndex].getTextResId();
            mQuestionTextView.setText(question);
        }


}
